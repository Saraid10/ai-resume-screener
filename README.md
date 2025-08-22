# 🤖 AI-Powered Resume Screener

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red.svg)](https://streamlit.io)

An intelligent web application built with Streamlit and Scikit-learn that automates the process of resume screening by calculating a similarity score between resumes and a given job description.



---

## ## 🎯 About The Project

In today's competitive job market, recruiters often receive hundreds of resumes for a single position. Manually screening these documents is time-consuming, tedious, and prone to human bias.

This AI-Powered Resume Screener is designed to solve that problem. By leveraging Natural Language Processing (NLP), the tool can quickly analyze and score multiple resumes against a job description, providing a ranked list of the most qualified candidates. This allows hiring managers to focus their time and attention on the best fits for the role.

### ## ✨ Features

-   **Job Description Input:** A simple text area to paste the job description.
-   **Multiple Resume Uploads:** Supports uploading multiple PDF resumes at once.
-   **NLP-Based Scoring:** Uses TF-IDF and Cosine Similarity to calculate a relevance score for each resume.
-   **Ranked Results:** Displays a clean, sorted table of candidates from best to worst match.
-   **Score Visualization:** Includes a bar chart for an intuitive visual comparison of candidate scores.

---

## ## 🛠️ Built With

This project is built with the following technologies:

-   **Python:** The core programming language.
-   **Streamlit:** For building the interactive web UI.
-   **Scikit-learn:** For TF-IDF vectorization and cosine similarity calculation.
-   **NLTK (Natural Language Toolkit):** For text preprocessing tasks like tokenization and stop-word removal.
-   **PyMuPDF:** For extracting text content from PDF files.

---

## ## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### ## Prerequisites

Make sure you have Python 3.9+ and `pip` installed on your system.

### ## Installation

1.  **Clone the repository**
    ```sh
    git clone [https://github.com/YourUsername/ai-resume-screener.git](https://github.com/YourUsername/ai-resume-screener.git)
    ```
2.  **Navigate to the project directory**
    ```sh
    cd ai-resume-screener
    ```
3.  **Create and activate a virtual environment**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```
4.  **Install the required dependencies**
    ```sh
    pip install -r requirements.txt
    ```

**Note:** The first time you run the application, it will automatically download the necessary NLTK language models. This might take a moment and will only happen once.

### ## Running the Application

1.  **Launch the Streamlit app**
    ```sh
    streamlit run app.py
    ```
2.  Open your web browser and go to `http://localhost:8501`.

---

## ## 📖 Usage

1.  Paste the job description into the text area on the left.
2.  Upload one or more candidate resumes (in PDF format) using the file uploader.
3.  Click the "Analyze Resumes" button.
4.  View the ranked list of candidates and the score visualization.

---

## ## 📄 License

This project is distributed under the MIT License. See `LICENSE` for more information.
