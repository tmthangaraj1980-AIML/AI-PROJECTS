# 🧠 ThangarajAI - AI Knowledge Hub

An AI-powered learning platform designed to help students, freshers, and aspiring AI professionals prepare for interviews and strengthen their understanding of Artificial Intelligence, Machine Learning, Data Science, Deep Learning, NLP, and Generative AI concepts.

---

## 🚀 Project Overview

ThangarajAI combines a curated AIML knowledge base with Generative AI capabilities to provide instant explanations and interview preparation support.

The application first searches a dataset of AIML interview questions and answers. If no suitable answer is found, it uses Gemini AI as a fallback to generate a relevant response.

---

## ✨ Features

* 500+ AIML Interview Questions and Answers
* Intelligent Question Matching
* AI-Powered Fallback Responses
* FAQ-Based Knowledge Retrieval
* Gemini AI Integration
* Streamlit Interactive Interface
* Random Interview Question Generator
* Recent Question History
* Beginner-Friendly Learning Platform
* Real-Time AI Assistance

---

## 📚 Topics Covered

### Python

* Variables and Data Types
* Functions
* OOP Concepts
* Exception Handling
* File Handling

### Machine Learning

* Supervised Learning
* Unsupervised Learning
* Regression
* Classification
* Model Evaluation
* Feature Engineering

### Deep Learning

* Neural Networks
* CNN
* RNN
* LSTM
* Transformers

### Natural Language Processing (NLP)

* Tokenization
* Stemming
* Lemmatization
* TF-IDF
* Word Embeddings

### Data Science

* Data Cleaning
* EDA
* Visualization
* Feature Selection
* Data Transformation

### Generative AI

* LLMs
* Prompt Engineering
* RAG
* Fine-Tuning
* Gemini AI

---

## 🛠️ Technology Stack

* Python
* Pandas
* Streamlit
* Difflib
* Google Gemini API
* Transformers (Optional)

---

## 📂 Project Structure

```text
01_ThangarajAI_Knowledge_Hub
│
├── app.py
├── ai_ml_ds_professor_faq_500.csv
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-PROJECTS.git
```

Navigate to project folder:

```bash
cd 01_ThangarajAI_chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🔑 Gemini API Configuration

This project uses Google's Gemini API for AI-powered fallback responses.

### Get Your Gemini API Key

Visit:

https://aistudio.google.com/app/apikey

Create your API key.

Configure it in your application:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

Recommended Model:

```python
model = genai.GenerativeModel("gemini-2.0-flash")
```

> Never upload your API key to GitHub repositories.

---

## 🧠 Intelligent Question Matching & AI Fallback

The system uses similarity matching to compare the user's question with the AIML FAQ dataset.

### Step 1: FAQ Search

* User enters a question.
* The system searches the dataset of 500+ AIML interview questions.
* Similarity matching is performed using Python's `difflib.get_close_matches()`.

### Step 2: Match Found

If a similar question is found:

* The corresponding answer from the dataset is returned instantly.
* This provides fast and accurate responses.

### Step 3: No Match Found

If no suitable question is found:

* The user's query is automatically forwarded to Gemini AI.
* Gemini generates a contextual response.
* The generated answer is displayed to the user.

### Workflow

```text
User Question
      ↓
FAQ Similarity Search
      ↓
Match Found?
├── YES → Return FAQ Answer
└── NO
      ↓
 Gemini AI
      ↓
 Generated Response
```

This hybrid architecture combines:

* Curated AIML Knowledge Base
* Intelligent Search
* Generative AI
* Improved User Experience

---

## 💡 Example Questions

* What is Machine Learning?
* What is Overfitting?
* Explain Random Forest.
* What is Logistic Regression?
* What is Feature Engineering?
* What is Prompt Engineering?
* Difference between CNN and RNN.
* What is Generative AI?
* Explain Gradient Descent.
* What is Cross Validation?

---

## 🎯 Use Cases

* AIML Interview Preparation
* Student Learning Assistance
* Quick Concept Revision
* AI Knowledge Exploration
* Self-Learning Platform
* Technical Question Answering

---

## 📈 Future Enhancements

* Voice Input Support
* Resume-Based Interview Questions
* AI Mock Interview System
* Topic-Based Filtering
* Multi-Language Support
* RAG-Based Knowledge Retrieval
* PDF Knowledge Base Integration
* Personalized Learning Recommendations

---

## 👨‍💻 Author

**Thangaraj T**

AI/ML Intern | Machine Learning Enthusiast | Generative AI Learner

GitHub Portfolio: AI-PROJECTS

---

## ⭐ Project Goal

To provide an interactive AI-powered learning platform that helps students and professionals prepare for AIML interviews while exploring Artificial Intelligence concepts through a hybrid knowledge retrieval and Generative AI approach.
