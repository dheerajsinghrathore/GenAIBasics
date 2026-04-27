from langchain_text_splitters import RecursiveCharacterTextSplitter
text="""Artificial Intelligence is changing the world by
          making technology smarter and more efficient. It
          helps automate many tasks that once required human effort,
          saving time and increasing productivity.
          In healthcare, AI assists doctors in diagnosing diseases
          and analyzing medical data.
          In business and finance, it helps analyze large amounts of information
          to make better decisions. AI is also improving everyday life through
          technologies like virtual assistants, recommendation systems,
          and self-driving cars.
"""
splitter=RecursiveCharacterTextSplitter(chunk_size=30,chunk_overlap=0)
chunks=splitter.split_text(text)
print(len(chunks))
print(chunks)
