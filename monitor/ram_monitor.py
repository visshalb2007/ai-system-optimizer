try:
    import psutil
except ImportError:
    print("psutil module is not installed. Install it with `pip install psutil`.")
    raise

ram = psutil.virtual_memory()

print(f"Total RAM: {round(ram.total / (1024**3), 2)} GB")
print(f"Used RAM: {round(ram.used / (1024**3), 2)} GB")
print(f"Available RAM: {round(ram.available / (1024**3), 2)} GB")
print(f"RAM Usage: {ram.percent}%")