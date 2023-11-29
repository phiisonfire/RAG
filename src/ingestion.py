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

file_path = "./data/llama2.pdf"
doc = fitz.open(file_path)

# Use a Text Splitter to Split Documents
from llama_index.text_splitter import SentenceSplitter

text_splitter = SentenceSplitter(
    chunk_size=1024
)

text_chunks = []
doc_idxs = []
for doc_idx, page in enumerate(doc):
    page_text = page.get_text("text")
    cur_text_chunk = text_splitter.split_text(page_text)
    text_chunks.extend(cur_text_chunk)
    doc_idxs.extend([doc_idx] * len(cur_text_chunk))

# 3. Manually Construct Nodes from Text Chunks
from llama_index.schema import TextNode

nodes = []
for idx, text_chunk in enumerate(text_chunks):
    node = TextNode(
        text=text_chunk,
    )
    src_doc_idx = doc_idxs[idx]
    src_page = doc[src_doc_idx]
    nodes.append(node)



