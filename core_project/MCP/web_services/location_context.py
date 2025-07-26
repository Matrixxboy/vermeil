import geocoder

def get_location_context():
    try:
        g = geocoder.ip('me')
        return f"Location: {g.city}, {g.country}"
    except Exception:
        return "Location: unknown"
