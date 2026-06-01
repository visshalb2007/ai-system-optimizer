import psutil

print("\nTop Running Processes:\n")

processes = []

for process in psutil.process_iter(['pid', 'name', 'memory_percent']):
    try:
        info = process.info

        processes.append({
            "pid": info['pid'],
            "name": info['name'],
            "memory": info['memory_percent']
        })

    except:
        pass

processes = sorted(processes, key=lambda x: x['memory'], reverse=True)

for process in processes[:10]:
    print(
        f"PID: {process['pid']} | "
        f"Name: {process['name']} | "
        f"RAM Usage: {process['memory']:.2f}%"
    )