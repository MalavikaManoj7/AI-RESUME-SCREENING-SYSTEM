from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def rank_candidates(tfidf_matrix, resumes_df):
    similarity_scores = cosine_similarity(tfidf_matrix[:-1], tfidf_matrix[-1])
    resumes_df["matching_score"] = similarity_scores.flatten()
    ranked_df = resumes_df.sort_values(by="matching_score", ascending=False)
    return ranked_df
