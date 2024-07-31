from typing import List
import psycopg2
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Enum, make_url
import pandas as pd
from pgvector.sqlalchemy import VECTOR
from sentence_transformers import SentenceTransformer
from ..base import VannaBase
from pgvector.psycopg2 import register_vector
import numpy as np

class PostgresVectorStore(VannaBase):
    """
    A class to manage a PostgreSQL vector store for various content types such as question-sql, ddl, and documentation.
    This class utilizes the pgvector extension and SentenceTransformer for embedding generation.
    """

    def __init__(self, connection_string, db_name, table_name, embed_dim, model_path="/home/hassant/.cache/chroma/onnx_models/local_model"):
        """
        Initialize the PostgresVectorStore.

        :param connection_string: Connection string to the PostgreSQL server.
        :param db_name: Database name.
        :param table_name: Table name to store the vectors.
        :param embed_dim: Dimension of the embeddings.
        :param model_path: Path to the SentenceTransformer model.
        """
        self.connection_string = connection_string
        self.db_name = db_name
        self.table_name = table_name
        self.embed_dim = embed_dim
        self.url = make_url(connection_string)
        
        # Ensure the pgvector extension is enabled
        self._ensure_extension()
        
        # Set up SQLAlchemy engine and metadata
        self.engine = create_engine(f"{self.connection_string}/{self.db_name}")
        self.metadata = MetaData()
        
        # Define the vector table schema
        self.vector_table = Table(
            self.table_name,
            self.metadata,
            Column('id', Integer, primary_key=True),
            Column('type', Enum('question-sql', 'ddl', 'documentation', 'general', name='content_type')),
            Column('description', String),
            Column('embedding', VECTOR(dim=embed_dim))
        )
        
        # Create the table if it doesn't exist
        self.metadata.create_all(self.engine)
        
        # Create an index on the embedding column
        self._create_index()
        
        # Load the embedding model
        self.embedding_model = SentenceTransformer(model_path)

    def _ensure_extension(self):
        """
        Ensure the pgvector extension is enabled in the PostgreSQL database.
        """
        try:
            conn = psycopg2.connect(f"{self.connection_string}/{self.db_name}")
            conn.autocommit = True
            register_vector(conn)
            with conn.cursor() as c:
                c.execute('CREATE EXTENSION IF NOT EXISTS vector')
        except Exception as e:
            print(f"Error ensuring extension: {e}")
        finally:
            conn.close()

    def _get_connection(self):
        """
        Get a connection to the PostgreSQL database.

        :return: psycopg2 connection object.
        """
        conn = psycopg2.connect(f"{self.connection_string}/{self.db_name}")
        register_vector(conn)
        return conn

    def _create_index(self):
        """
        Create an index on the embedding column using ivfflat method.
        """
        try:
            with self._get_connection() as conn:
                with conn.cursor() as c:
                    c.execute(f'CREATE INDEX IF NOT EXISTS idx_{self.table_name}_embedding ON {self.table_name} USING ivfflat (embedding vector_l2_ops) WITH (lists = 100)')
        except Exception as e:
            print(f"Error creating index: {e}")

    def generate_embedding(self, data: str, **kwargs) -> List[float]:
        """
        Generate an embedding for the given data using SentenceTransformer.

        :param data: Data to be embedded.
        :return: Embedding as a list of floats.
        """
        embeddings = self.embedding_model.encode(data)
        return embeddings.tolist()

    def get_training_data(self, **kwargs) -> pd.DataFrame:
        """
        Retrieve all training data from the table.

        :return: Data as a pandas DataFrame.
        """
        query = f"SELECT * FROM {self.table_name}"
        with self.engine.connect() as conn:
            df = pd.read_sql(query, conn)
        return df

    def remove_training_data(self, id: str, **kwargs) -> bool:
        """
        Remove training data by ID.

        :param id: ID of the data to be removed.
        :return: True if the data was successfully removed, False otherwise.
        """
        query = f"DELETE FROM {self.table_name} WHERE id=%s"
        with self._get_connection() as conn:
            with conn.cursor() as c:
                c.execute(query, (id,))
                return c.rowcount > 0

    def remove_collection(self, collection_name: str) -> bool:
        """
        Remove all entries of a specific content type.

        :param collection_name: Content type to be removed.
        :return: True if the collection was successfully removed, False otherwise.
        """
        try:
            query = f"DELETE FROM {self.table_name} WHERE type=%s"
            with self._get_connection() as conn:
                with conn.cursor() as c:
                    c.execute(query, (collection_name,))
            return True
        except Exception as e:
            print(f"Error removing collection: {e}")
            return False

    def add_question_sql(self, question: str, sql: str, **kwargs) -> str:
        """
        Add a question-SQL pair to the table.

        :param question: The question.
        :param sql: The SQL statement.
        :return: Success message.
        """
        entry = f'"question": {question}, "sql": {sql}'
        return self.add_entry("question-sql", entry, **kwargs)

    def add_ddl(self, ddl: str, **kwargs) -> str:
        """
        Add a DDL statement to the table.

        :param ddl: The DDL statement.
        :return: Success message.
        """
        return self.add_entry("ddl", ddl, **kwargs)

    def add_documentation(self, documentation: str, **kwargs) -> str:
        """
        Add documentation to the table.

        :param documentation: The documentation.
        :return: Success message.
        """
        return self.add_entry("documentation", documentation, **kwargs)

    def get_similar_question_sql(self, question: str, **kwargs) -> list:
        """
        Get similar question-SQL pairs from the table.

        :param question: The question to find similarities for.
        :return: List of similar question-SQL pairs.
        """
        return self.get_related_entries(question, content_type="question-sql", **kwargs)

    def get_related_ddl(self, question: str, **kwargs) -> list:
        """
        Get related DDL statements from the table.

        :param question: The question to find similarities for.
        :return: List of related DDL statements.
        """
        return self.get_related_entries(question, content_type="ddl", **kwargs)

    def get_related_documentation(self, question: str, **kwargs) -> list:
        """
        Get related documentation from the table.

        :param question: The question to find similarities for.
        :return: List of related documentation.
        """
        return self.get_related_entries(question, content_type="documentation", **kwargs)

    def add_entry(self, content_type: str, description: str, **kwargs) -> str:
        """
        Add an entry to the table.

        :param content_type: Type of the content (e.g., question-sql, ddl, documentation).
        :param description: Description of the content.
        :return: Success message.
        """
        embedding = self.generate_embedding(description)
        query = f"INSERT INTO {self.table_name} (type, description, embedding) VALUES (%s, %s, %s)"
        with self._get_connection() as conn:
            with conn.cursor() as c:
                c.execute(query, (content_type, description, embedding))
        return f"{content_type.capitalize()} added successfully"

    def get_related_entries(self, description: str, content_type: str = None, **kwargs) -> list:
        """
        Get related entries from the table based on the description.

        :param description: Description to find similarities for.
        :param content_type: Type of content to filter by.
        :return: List of related entries.
        """
        embedding = self.generate_embedding(description)
        embedding_str = f"ARRAY{embedding}"
        query = f"SELECT type, description FROM {self.table_name} "
        if content_type:
            query += f"WHERE type = '{content_type}' "
        query += f"ORDER BY embedding <-> {embedding_str}::vector LIMIT 5"

        with self._get_connection() as conn:
            with conn.cursor() as c:
                c.execute(query)
                result = c.fetchall()
        return [row[1] for row in result]

# Vector Operators:
# Operator     Description
# +            Element-wise addition
# -            Element-wise subtraction
# *            Element-wise multiplication 
# ||           Concatenate 
# <->          Euclidean distance
# <#>          Negative inner product
# <=>          Cosine distance
# <+>          Taxicab distance 
