from langchain_text_splitter import CharacterTextSplitter
text = "This is an example of a long text that needs to be split into smaller chunks for processing. The text splitter will help us divide this text into manageable pieces."
text_splitter = CharacterTextSplitter(chunk_size=30, chunk_overlap=0)
chunks = text_splitter.split_text(text)
print(len(chunks))