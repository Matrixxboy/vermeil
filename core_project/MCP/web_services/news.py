import feedparser

def get_news_context(text=None):
    """
    Fetches top headlines from Google News RSS.
    """
    try:
        # Google News RSS (World)
        rss_url = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
        feed = feedparser.parse(rss_url)
        
        if not feed.entries:
            return "News: No news found."

        # Get top 3 headlines
        headlines = []
        for entry in feed.entries[:3]:
            headlines.append(f"- {entry.title}")
        
        return "Latest News:\n" + "\n".join(headlines)
    except Exception as e:
        return f"News: Error fetching news - {str(e)}"
