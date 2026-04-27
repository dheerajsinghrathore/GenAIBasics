from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Step 1: Convert pdf into Documents
loader = PyPDFLoader("policy.pdf")
docs = loader.load()

# Step 2: Split into Chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

chunks = splitter.split_documents(docs)

# Step 3: Create embeddings

embeddings = OpenAIEmbeddings()

# Step 4: Persistent DB
vectorstore = Chroma.from_documents(
    documents=chunks, embedding=embeddings, persist_directory="./db"
)

# Step 5: Create Retriever
retriever = vectorstore.as_retriever()

# Step 5 Prompt template
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions only on the context below:
    {context}
    Question:{question}
    """
)

# Step 7 LLM
llm = ChatOpenAI(model="gpt-4o-mini")


# step 8
def format_docs(docs):
    return "\n\n".join(f"-{doc.page_content}" for doc in docs)


# Step 9 : RAG Pipeline

while True:
    query = input("\nAsk Something(exit to quit):")
    if query.lower() == "exit":
        break
    retrieved_docs = retriever.invoke(query)

    # combine context
    context = format_docs(retrieved_docs)

    # Create the final prompt
    final_prompt = prompt.format(context=context, question=query)

    # Generate Answer
    response = llm.invoke(final_prompt)
    print("\nAnswer:", response.content)
