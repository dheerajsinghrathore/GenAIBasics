import streamlit as st
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
from docx import Document

load_dotenv()


# Step 1: Define the state of the graph
class State(TypedDict):
    resume: str
    analysis: str
    feedback: str
    count: int

# Step 2: Create the LLM and the graph
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)


# Step 3: Define the Nodes
def analyze_resume(state):
    prompt = f"""Analyze the following resume and provide feedback:
    Focus on the following aspects:
    - Skills
    - Experience
    - Projects
    - Education
    - Overall presentation

    Resume:
    {state['resume']}
    Give atleast 5 points of feedback and suggestions for improvement.
"""
    if state["feedback"]:
        prompt += f"\nPrevious feedback: {state['feedback']}\n"
    response = llm.invoke(prompt)
    return {"analysis": response.content, "count": state["count"] + 1}


def review_analysis(state):
    text = state["analysis"] or ""
    if len(text) < 200:
        return {"feedback": "The analysis is too brief. Please provide more detailed feedback."}
    if "skills" not in text.lower():
        return {"feedback": "The analysis should include a section on skills."}
    return {"feedback": "good"}


# Step 4: Decision Nodes
def should_continue(state):
    if state["count"] >= 3 and state["feedback"] == "good":
        return "end"
    return "retry"


# Step 5: Build the Graph
builder = StateGraph(State)
builder.add_node("analyze", analyze_resume)
builder.add_node("review", review_analysis)

builder.add_edge(START, "analyze")
builder.add_edge("analyze", "review")

builder.add_conditional_edges(
    "review", should_continue, {"end": END, "retry": "analyze"}
)

graph = builder.compile()
# Step 6: Streamlit UI
st.set_page_config(page_title="AI Resume Analyzer", layout="centered", page_icon="📄")
st.title("AI Resume Analyzer (LangGraph + LLM)")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF or DOCX)", type=["pdf", "docx"], key="resume_file"
)
resume_text = ""
# Check if a file is uploaded
if uploaded_file is not None:
    # Process PDF files
    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        resume_text = text
    # Process DOCX files
    elif (
        uploaded_file.type
        == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ):
        doc = Document(uploaded_file)
        text = []
        for para in doc.paragraphs:
            text.append(para.text)
        resume_text = "\n".join(text)
    elif uploaded_file.type == "text/plain":
        resume_text = uploaded_file.read().decode("utf-8")
    st.success("Resume uploaded successfully!")

if st.button("Analyze Resume"):
    if resume_text:
        with st.spinner("Analyzing resume..."):
            result = graph.invoke({"resume": resume_text, "analysis": "", "feedback": "", "count": 0})
        st.success("Analysis complete! ✅")
        st.subheader("💡 Suggestions")
        st.write(result["analysis"])
        st.subheader("🔍 Feedback")
        st.write(result["feedback"])
        st.subheader("👀 Attempts Used")
        st.write(result["count"])
    else:
        st.warning("Please upload a resume before analyzing.")