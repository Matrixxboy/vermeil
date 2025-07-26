from datetime import datetime

def get_time_context():
    now = datetime.now()
    return f"Time: {now.strftime('%A, %B %d, %Y %I:%M %p')}"
