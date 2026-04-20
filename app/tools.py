from langchain.tools import tool

@tool
def mock_searxng_search(query: str):
    """Mock search tool that returns fake news headlines based on query keywords."""
    
    query = query.lower()

    if "crypto" in query:
        return "Bitcoin hits new all-time high amid ETF approvals"
    elif "ai" in query:
        return "OpenAI releases new model replacing junior developers"
    elif "market" in query:
        return "Federal Reserve signals possible interest rate cuts"
    
    return "Global economy remains uncertain"