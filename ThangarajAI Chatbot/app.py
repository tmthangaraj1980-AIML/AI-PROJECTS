import streamlit as st
import pandas as pd
import google.generativeai as genai
from difflib import get_close_matches
import os

# ✅ Configure Gemini securely
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

# ✅ Load dataset
faq = pd.read_csv("ai_ml_ds_professor_faq_500.csv")

# ✅ Chatbot logic
def chatbot(query):
    # 1. Clean the incoming question (remove bullet dots, spaces, lowercase it)
    cleaned_query = query.replace("•", "").replace("-", "").strip().lower()
    
    # 2. Build a lowercase mapping of your dataset
    # format: { "what is machine learning?": "What is Machine Learning?" }
    questions_dict = {
        str(q).replace("•", "").replace("-", "").strip().lower(): q 
        for q in faq['question'].tolist()
    }
    
    # 3. Check for an EXACT structural match first
    if cleaned_query in questions_dict:
        original_question = questions_dict[cleaned_query]
        return faq.loc[faq['question'] == original_question, 'answer'].values[0]
        
    # 4. If it isn't an exact match, check for a close match with a strict 0.75+ cutoff
    match = get_close_matches(cleaned_query, list(questions_dict.keys()), n=1, cutoff=0.75)
    if match:
        original_question = questions_dict[match[0]]
        return faq.loc[faq['question'] == original_question, 'answer'].values[0]
        
    # 5. Fallback completely to Gemini if it's outside the FAQ scope
    try:
        response = model.generate_content(query)
        return response.text
    except Exception:
        return "AI fallback is temporarily unavailable due to API quota limit. Please try again later."

# ✅ Streamlit UI
st.set_page_config(
    page_title="ThangarajAI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# --- SIDEBAR ---
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

# --- MAIN PAGE HEADERS ---
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

# --- CHAT UTILITY LOGIC ---
# Initialize session state to keep track of the current question and answer
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "current_response" not in st.session_state:
    st.session_state.current_response = None

# ✅ Using st.chat_input: This clears automatically upon pressing Enter or clicking send!
user_input = st.chat_input("Ask your interview question here...")

if user_input:
    st.session_state.current_question = user_input
    with st.spinner("Thinking..."):
        st.session_state.current_response = chatbot(user_input)

# --- DISPLAY RESPONSE ---
if st.session_state.current_question:
    # Optional: Display the user's question back to them in a chat bubble
    with st.chat_message("user"):
        st.write(st.session_state.current_question)
        
    st.markdown("### 💡 Response")
    with st.chat_message("assistant"):
        st.success(st.session_state.current_response)

st.markdown("---")
st.caption("Developed by Thangaraj | AIML Intern | Built with Python & Streamlit")