from googlesearch import search

def get_web_search_context(text):
    """
    Performs a Google search and returns top result titles/URLs.
    """
    try:
        query = text.lower().replace("search", "").replace("google", "").strip()
        if not query:
            return "Web Search: No query provided."

        results = []
        # Fetch top 3 results
        for item in search(query, advanced=True, num_results=3):
            results.append(f"{item.title}: {item.description} ({item.url})")
            if len(results) >= 3:
                break
        
        if not results:
             return f"Web Search: No results for '{query}'"

        return f"Web Search Results for '{query}':\n" + "\n".join(results)
    except Exception as e:
        return f"Web Search: Error - {str(e)}"
