from fastapi import FastAPI
from ingestion import fetch_papers
from summarizer import summarize_paper

app = FastAPI()

@app.get("/papers")
def get_papers(query: str):
    papers = fetch_papers(query)
    for paper in papers:
        paper["summary"] = summarize_paper(paper["title"], paper["summary"])
    return papers
