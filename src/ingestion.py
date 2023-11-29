import os
from dotenv import load_dotenv
import pinecone
from llama_index.vector_stores import PineconeVectorStore
import fitz

load_dotenv(dotenv_path='.env')
api_key = os.environ["PINECONE_API_KEY"]
environment = os.environ["PINECONE_ENVIRONMENT"]
pinecone.init(api_key=api_key, environment=environment)

index_name = "llamaindex-rag-fs"

pinecone.create_index(
    index_name, dimension=1536, metric='euclidean', pod_type='p1'
)

pinecone_index = pinecone.Index(index_name=index_name)

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)



