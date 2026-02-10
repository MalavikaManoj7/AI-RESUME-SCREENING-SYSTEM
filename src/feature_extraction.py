from sklearn.feature_extraction.text import TfidfVectorizer

def extract_features(resume_texts, job_text):
    corpus = resume_texts + [job_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    return tfidf_matrix
