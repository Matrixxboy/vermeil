import psutil

def get_system_context():
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)
    return f"System: {mem.available // (1024**2)}MB free RAM, CPU usage {cpu}%"
