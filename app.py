import streamlit as st
import fitz  # PyMuPDF
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import nltk

# --- Self-healing NLTK data download ---
# This block ensures the necessary NLTK data is available.
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    st.info("First-time setup: Downloading necessary NLTK data...")
    st.info("This will only happen once.")
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    st.success("Downloads complete! The app is ready.")
# --- End of block ---


# --- CORE NLP FUNCTIONS ---

def extract_text_from_pdf(file_bytes):
    """Extracts text from a PDF file's bytes."""
    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return ""

def preprocess_text(text):
    """Cleans and preprocesses the text."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return " ".join(filtered_tokens)

def calculate_similarity(resume_text, jd_text):
    """Calculates cosine similarity between two texts using TF-IDF."""
    processed_resume = preprocess_text(resume_text)
    processed_jd = preprocess_text(jd_text)
    
    corpus = [processed_resume, processed_jd]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    
    return cosine_sim

# --- STREAMLIT UI ---

st.set_page_config(layout="wide", page_title="AI Resume Screener")

st.title("🤖 AI-Powered Resume Screener")
st.markdown("This tool ranks resumes against a job description to find the best candidates instantly.")

st.sidebar.header("How it Works")
st.sidebar.info(
    "1. Paste the job description in the text area.\n"
    "2. Upload one or more resumes (PDF format).\n"
    "3. Click 'Analyze Resumes' to see the similarity scores.\n"
    "4. The app uses TF-IDF and Cosine Similarity to score resumes based on keyword relevance."
)

st.header("1. Job Description")
job_description = st.text_area("Paste the full job description here:", height=250, placeholder="e.g., Seeking a Python developer with experience in Streamlit and NLP...")

st.header("2. Upload Resumes")
uploaded_resumes = st.file_uploader(
    "Upload candidate resumes here (PDF files only).", 
    type="pdf", 
    accept_multiple_files=True
)

if st.button("Analyze Resumes", type="primary"):
    if not job_description.strip():
        st.warning("Please paste a job description first.")
    elif not uploaded_resumes:
        st.warning("Please upload at least one resume.")
    else:
        with st.spinner("Analyzing... This may take a moment."):
            results = []
            
            for resume_file in uploaded_resumes:
                resume_bytes = resume_file.read()
                resume_text = extract_text_from_pdf(resume_bytes)
                
                if resume_text:
                    similarity_score = calculate_similarity(resume_text, job_description)
                    results.append({
                        "filename": resume_file.name,
                        "score": similarity_score
                    })
            
            if results:
                results_df = pd.DataFrame(results).sort_values(by="score", ascending=False).reset_index(drop=True)
                
                st.success("Analysis Complete!")
                
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.header("🏆 Ranked Results")
                    display_df = results_df.copy()
                    display_df["score"] = display_df["score"].apply(lambda x: f"{x:.2%}")
                    st.dataframe(display_df, use_container_width=True)

                with col2:
                    st.header("📊 Score Visualization")
                    chart_df = results_df.set_index('filename')
                    st.bar_chart(chart_df)
            else:
                st.error("Could not process any of the uploaded resumes. Please check the file formats.")