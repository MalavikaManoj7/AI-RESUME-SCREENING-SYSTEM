import streamlit as st
import pandas as pd

from src.text_preprocessing import preprocess_text
from src.feature_extraction import extract_features
from src.ranking import rank_candidates

# Page config
st.set_page_config(page_title="AI Resume Screening System", layout="centered")

# Title
st.title("🤖 AI-Powered Resume Screening System")
st.subheader("HR Analytics using NLP & Machine Learning")

st.write("Upload resumes and enter a job description to rank candidates automatically.")

# Upload resumes
uploaded_file = st.file_uploader("Upload Resume Dataset (CSV)", type=["csv"])

# Job description input
job_description = st.text_area(
    "Enter Job Description",
    height=150,
    placeholder="Enter required skills, qualifications, and experience..."
)

# Button
if st.button("🔍 Rank Candidates"):

    if uploaded_file is None or job_description.strip() == "":
        st.warning("⚠️ Please upload resumes and enter a job description.")
    else:
        # Load resumes
        resumes = pd.read_csv(uploaded_file)

        # Combine text fields
        resumes["resume_text"] = resumes["skills"] + " " + resumes["education"]

        # Preprocess resumes
        resumes["clean_text"] = resumes["resume_text"].apply(preprocess_text)
        clean_job_desc = preprocess_text(job_description)

        # Feature extraction
        tfidf_matrix = extract_features(
            resumes["clean_text"].tolist(),
            clean_job_desc
        )

        # Ranking
        ranked_candidates = rank_candidates(tfidf_matrix, resumes)

        # Display results
        st.success("✅ Candidate Ranking Completed!")
        st.dataframe(
            ranked_candidates[["name", "matching_score"]],
            use_container_width=True
        )

        # Download option
        csv = ranked_candidates.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="⬇️ Download Ranked Candidates",
            data=csv,
            file_name="ranked_candidates.csv",
            mime="text/csv"
        )
