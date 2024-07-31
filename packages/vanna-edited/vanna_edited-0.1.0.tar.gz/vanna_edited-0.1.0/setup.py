from setuptools import setup, find_packages

setup(
    name='vanna-edited',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'psycopg2',
        'pgvector',
        'sentence-transformers',
        'vanna'
    ],
    description='An edited vanna package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Hassan Tfaily',
    author_email='hassantfaily@icloud.com',
    url='https://github.com/hassantfaily/vanna',  # Update with the actual URL
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    extras_require={
        'postgres': ["psycopg2-binary", "db-dtypes"],
        'mysql': ["PyMySQL"],
        'clickhouse': ["clickhouse_connect"],
        'bigquery': ["google-cloud-bigquery"],
        'snowflake': ["snowflake-connector-python"],
        'duckdb': ["duckdb"],
        'google': ["google-generativeai", "google-cloud-aiplatform"],
        'all': [
            "psycopg2-binary", "db-dtypes", "PyMySQL", "google-cloud-bigquery",
            "snowflake-connector-python", "duckdb", "openai", "mistralai",
            "chromadb", "anthropic", "zhipuai", "marqo", "google-generativeai",
            "google-cloud-aiplatform", "qdrant-client", "fastembed", "ollama",
            "httpx", "opensearch-py", "opensearch-dsl", "transformers",
            "pinecone-client", "pymilvus[model]", "weaviate-client"
        ],
        'test': ["tox"],
        'chromadb': ["chromadb"],
        'openai': ["openai"],
        'mistralai': ["mistralai"],
        'anthropic': ["anthropic"],
        'gemini': ["google-generativeai"],
        'marqo': ["marqo"],
        'zhipuai': ["zhipuai"],
        'ollama': ["ollama", "httpx"],
        'qdrant': ["qdrant-client", "fastembed"],
        'vllm': ["vllm"],
        'pinecone': ["pinecone-client", "fastembed"],
        'opensearch': ["opensearch-py", "opensearch-dsl"],
        'hf': ["transformers"],
        'milvus': ["pymilvus[model]"],
        'bedrock': ["boto3", "botocore"],
        'weaviate': ["weaviate-client"]
    }
)
