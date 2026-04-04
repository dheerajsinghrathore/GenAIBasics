from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import numpy as np
import os
load_dotenv()
emb = OpenAIEmbeddings()
v1 = emb.embed_query("What is RAG?")
v2 = emb.embed_query("What is Retrieval Augmented Generation?")
similarity = np.dot(v1, v2)/np.linalg.norm(v1)/np.linalg.norm(v2)
print(len(v1))
print(len(v2))
print(similarity)