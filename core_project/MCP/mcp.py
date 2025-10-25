from .user_utilities.timing_context import get_time_context
from .web_services.weather import get_weather_context
from .system_control.system_status import get_system_context
from .web_services.location_context import get_location_context
# from .web_services.command import open_website , search_web , search_youtube , open_whatsapp
# MCP Map: Name → Callable
MCP_FUNCTIONS = {
    "time": get_time_context,
    "weather": get_weather_context,
    "system": get_system_context,
    "location": get_location_context,
}

def collect_contexts(selected: list[str] = None) -> str:
    """
    Collect selected MCP contexts. If none are selected, return all.
    """
    selected = selected or MCP_FUNCTIONS.keys()
    contexts = []
    for name in selected:
        func = MCP_FUNCTIONS.get(name)
        if func:
            try:
                contexts.append(func())
            except Exception as e:
                contexts.append(f"[{name} context unavailable: {e}]")
    return "\n".join(contexts)
