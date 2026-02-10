import pandas as pd
from src.text_preprocessing import preprocess_text
from src.feature_extraction import extract_features
from src.ranking import rank_candidates

# Load data
resumes = pd.read_csv("data/resumes.csv")

with open("data/job_description.txt", "r") as file:
    job_description = file.read()

# Combine resume text
resumes["resume_text"] = resumes["skills"] + " " + resumes["education"]

# Preprocess text
resumes["clean_text"] = resumes["resume_text"].apply(preprocess_text)
clean_job_desc = preprocess_text(job_description)

# Feature extraction
tfidf_matrix = extract_features(resumes["clean_text"].tolist(), clean_job_desc)

# Ranking
ranked_candidates = rank_candidates(tfidf_matrix, resumes)

# Save results
ranked_candidates.to_csv("results/ranked_candidates.csv", index=False)

print("Candidate Ranking Completed!")
print(ranked_candidates[["name", "matching_score"]])
