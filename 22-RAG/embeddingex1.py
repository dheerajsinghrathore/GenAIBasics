from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
emb = OpenAIEmbeddings()
v1 = emb.embed_query("What is RAG?")
v2 = emb.embed_query("What is Retrieval Augmented Generation?")
print(len(v1))
print(len(v2))