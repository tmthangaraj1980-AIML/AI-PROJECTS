# app.py
import streamlit as st
import pandas as pd
import google.generativeai as genai
from difflib import get_close_matches
import os

# ✅ Configure Gemini securely (reads from environment variable)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


# ✅ Load dataset
faq = pd.read_csv("ai_ml_ds_professor_faq_500.csv")

# ✅ Chatbot logic (Step 2 + Step 2a combined)
def chatbot(query):
    questions = faq['question'].tolist()
    match = get_close_matches(query, questions, n=1, cutoff=0.4)
    if match:
        answer = faq.loc[faq['question'] == match[0], 'answer'].values[0]
        return answer
    try:
        response = model.generate_content(query)
        return response.text
    except Exception:
        return "AI fallback is temporarily unavailable due to API quota limit. Please try again later or ask another FAQ-based question."

# ✅ Streamlit UI
st.set_page_config(
    page_title="ThangarajAI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.title("🤖 ThangarajAI")
st.sidebar.markdown("### AIML Interview Assistant")
st.sidebar.write("Professor-style AI/ML Assistant")

st.sidebar.markdown("---")
st.sidebar.subheader("📌 Topics Covered")
st.sidebar.write("""
- Python
- Machine Learning
- Deep Learning
- NLP
- Data Science
- Generative AI
""")

st.sidebar.markdown("---")
st.sidebar.subheader("💡 Sample Questions")
st.sidebar.write("""
• What is Machine Learning?  
• What is Overfitting?  
• Explain Random Forest  
• What is NLP?  
• What is Prompt Engineering?
""")

st.title("🎯 ThangarajAI - AIML Interview Assistant")
st.write("Ask AI/ML/Data Science interview questions and get professor-style answers.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Questions", "500+")

with col2:
    st.metric("Topics", "AI / ML / DS")

with col3:
    st.metric("Mode", "FAQ + AI Fallback")

st.markdown("---")

st.subheader("💬 Ask Your Question")

user_input = st.text_area(
    "Enter your question:",
    height=100,
    placeholder="Example: What is the difference between supervised and unsupervised learning?"
)

if user_input:
    with st.spinner("Thinking..."):
        response = chatbot(user_input)

    st.markdown("### 💡 Response")
    st.success(response)

st.markdown("---")
st.caption("Developed by Thangaraj | AIML Intern | Built with Python & Streamlit")
