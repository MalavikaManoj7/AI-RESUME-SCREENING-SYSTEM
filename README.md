# AI-RESUME-SCREENING-SYSTEM
An intelligent resume screening system that uses Machine Learning & NLP to automatically analyze resumes and match them with job descriptions. This helps recruiters shortlist candidates faster and more accurately.
In simple words, This project automates resume screening using NLP and Machine Learning.
It extracts key information from resumes, matches them with job descriptions,
and ranks candidates based on relevance.

## Problem Statement

Recruiters often receive hundreds of resumes for a single job role. Manually reviewing each resume is:

Time-consuming

Error-prone

Inconsistent

There is a need for an automated system that can evaluate resumes based on job requirements and rank candidates accordingly.

## Proposed Solution

This project builds an AI-based Resume Screening System that:

✔ Extracts text from resumes
✔ Processes and cleans resume content
✔ Compares resumes with job descriptions
✔ Calculates a match score
✔ Ranks candidates based on suitability

The system is deployed as a Streamlit web application for easy use by recruiters.

## Key Features

📄 Resume text extraction

🧹 Text preprocessing using NLP

🧠 Machine Learning / Similarity-based scoring

📊 Resume-to-job description matching

🏆 Candidate ranking based on match percentage

🌐 Interactive web interface using Streamlit

## Technologies Used 
| Category             | Tools & Libraries                          |
| -------------------- | ------------------------------------------ |
| Programming          | Python                                     |
| Development          | Google Colab                               |
| Web App              | Streamlit                                  |
| Data Handling        | Pandas, NumPy                              |
| NLP                  | NLTK / spaCy / TF-IDF (whichever you used) |
| ML                   | Scikit-learn                               |
| Visualization        | Matplotlib / Seaborn                       |
| Deployment (Testing) | Ngrok                                      |

## How the System Works

1️⃣ Recruiter enters or uploads a Job Description
2️⃣ System processes the job description text
3️⃣ Multiple resumes are uploaded
4️⃣ Text is extracted and cleaned
5️⃣ AI model compares resumes with job description
6️⃣ Each resume gets a match score (%)
7️⃣ Resumes are ranked from best match to least match

## Project Workflow 
Data Collection (Resumes + Job Description)
        ↓
Text Extraction
        ↓
Text Preprocessing (Tokenization, Stopword Removal, etc.)
        ↓
Feature Extraction (TF-IDF / NLP vectors)
        ↓
Similarity / ML Model
        ↓
Score Calculation
        ↓
Ranking & Display in Streamlit App

## Running the project 

1. Clone the repository:
   git clone https://github.com/yourusername/ai-resume-screening-system.git
cd ai-resume-screening-system

2. Install requirements:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app.py

## Deployment

This project was tested using Ngrok to temporarily deploy the Streamlit application and access it via a public link.


 
