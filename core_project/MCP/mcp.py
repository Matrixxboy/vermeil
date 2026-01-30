from .user_utilities.timing_context import get_time_context
from .web_services.weather import get_weather_context
from .system_control.system_status import get_system_context
from .web_services.location_context import get_location_context
from .web_services.command import open_website, search_youtube, open_whatsapp
from .web_services.news import get_news_context
from .web_services.wikipedia_search import get_wiki_context
from .web_services.web_search import get_web_search_context

# MCP Map: Name → Callable
MCP_FUNCTIONS = {
    # Context Providers (No Input Needed)
    "time": get_time_context,
    "weather": get_weather_context,
    "system": get_system_context,
    "location": get_location_context,
    "news": get_news_context,
    
    # Action/Context Providers (Input Needed)
    "wiki": get_wiki_context,
    "web_search": get_web_search_context,
    "open_site": open_website,
    "youtube": search_youtube,
    "whatsapp": open_whatsapp,
}

# Functions that require user input
INPUT_REQUIRED = {
    "wiki",
    "web_search",
    "open_site",
    "youtube"
}

def collect_contexts(selected: list[str] = None, user_input: str = "") -> str:
    """
    Collect selected MCP contexts. If none are selected, return all.
    Passes user_input to functions that require it.
    """
    selected = selected or MCP_FUNCTIONS.keys()
    contexts = []
    
    for name in selected:
        func = MCP_FUNCTIONS.get(name)
        if func:
            try:
                # Pass user_input if the function expects it (based on a simple list or introspection)
                # Here we use a set for defined functions requiring input
                if name in INPUT_REQUIRED:
                     result = func(user_input)
                else:
                     result = func()
                
                contexts.append(result)
            except Exception as e:
                contexts.append(f"[{name} context unavailable: {e}]")
                
    return "\n".join(contexts)
