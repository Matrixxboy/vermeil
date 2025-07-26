from .user_utilities.timing_context import get_time_context
from .web_services.weather import get_weather_context
from .web_services.location_context import get_location_context
from .system_control.system_status import get_system_context

def collect_contexts():
    return "\n".join([
        get_time_context(),
        get_weather_context(),
        get_system_context(),
        get_location_context()
    ])
