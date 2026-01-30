import webbrowser
import re

def open_website(text):
    match = re.search(r"open (.+)", text.lower())
    if match:
        site = match.group(1).replace(" ", "")
        url = f"https://{site}.com" if "." not in site else f"https://{site}"
        webbrowser.open(url)
        return f"Command: Opening {url}"
    return "Command: Which site should I open?"

def search_web_action(text): # Renamed to avoid partial conflict with context search
    match = re.search(r"search for (.+)", text.lower())
    if match:
        query = match.group(1)
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Command: Searching Google for {query}"
    return "Command: What do you want to search for?"

def search_youtube(text):
    match = re.search(r"(youtube|play) (.+)", text.lower())
    if match:
        query = match.group(2)
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return f"Command: Searching YouTube for {query}"
    return "Command: What should I search on YouTube?"

def open_whatsapp(text=None):
    webbrowser.open("https://web.whatsapp.com/")
    return "Command: Opening WhatsApp Web..."
