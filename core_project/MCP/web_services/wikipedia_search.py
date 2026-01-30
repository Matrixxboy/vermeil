import wikipedia

def get_wiki_context(text):
    """
    Extracts a query from the text (simplified) and searches Wikipedia.
    Expects text like "who is X" or "tell me about Y".
    """
    try:
        # Simple heuristic to clean up the query
        # Remove common phrases to find the subject
        query = text.lower()
        remove_phrases = ["who is", "what is", "tell me about", "search for", "wiki", "wikipedia"]
        for phrase in remove_phrases:
            query = query.replace(phrase, "")
        
        query = query.strip()
        
        if not query:
            return "Wikipedia: No query found."

        # Limit to 2 sentences for brevity in context
        summary = wikipedia.summary(query, sentences=2)
        return f"Wikipedia Summary for '{query}': {summary}"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Wikipedia: Ambiguous term '{query}'. Options: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return f"Wikipedia: Page '{query}' not found."
    except Exception as e:
        return f"Wikipedia: Error - {str(e)}"
