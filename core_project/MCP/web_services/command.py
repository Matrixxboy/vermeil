import webbrowser
import os
import re

def parse_command(self, text: str):
    text = text.lower().strip()
    for keyword in self.commands.keys():
        if keyword in text:
            return self.commands[keyword], text
    return None, text

def execute(self, text: str):
    func, raw = self.parse_command(text)
    if func:
        return func(raw)
    else:
        return f"Sorry, I didn’t understand the command: {text}"

def open_website(self, text):
    match = re.search(r"open (.+)", text)
    if match:
        site = match.group(1).replace(" ", "")
        url = f"https://{site}.com" if "." not in site else site
        webbrowser.open(url)
        return f"Opening {url}"
    return "Which site should I open?"

def search_web(self, text):
    match = re.search(r"search (.+)", text)
    if match:
        query = match.group(1)
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching Google for {query}"
    return "What do you want to search for?"

def search_youtube(self, text):
    match = re.search(r"(youtube|search on youtube|play) (.+)", text)
    if match:
        query = match.group(2)
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return f"Searching YouTube for {query}"
    return "What should I search on YouTube?"

def open_whatsapp(self, text):
    webbrowser.open("https://web.whatsapp.com/")
    return "Opening WhatsApp Web..."
