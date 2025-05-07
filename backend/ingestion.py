import arxiv

def fetch_papers(query="reinforcement learning", max_results = 5):
    search = arxiv.Search(
        query=query,
        max_results = max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    papers = []
    for result in search.results():
        papers.append({
            "title": result.title,
            "summary": result.summary,
            "pdf_url": result.pdf_url,
            "published": result.published.strftime("%Y-%m-%d"),
        })
    
    return papers