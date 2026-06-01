import psutil
import time
import os

while True:
    os.system('cls')

    # RAM INFO
    ram = psutil.virtual_memory()

    print("=" * 50)
    print(" AI SYSTEM OPTIMIZER DASHBOARD ")
    print("=" * 50)

    print(f"\nRAM Usage: {ram.percent}%")
    print(f"Used RAM: {round(ram.used / (1024**3), 2)} GB")
    print(f"Available RAM: {round(ram.available / (1024**3), 2)} GB")

    # CPU INFO
    cpu = psutil.cpu_percent(interval=1)

    print(f"\nCPU Usage: {cpu}%")

    # TOP PROCESSES
    print("\nTop Processes:\n")

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

    processes = sorted(
        processes,
        key=lambda x: x['memory'],
        reverse=True
    )

    for process in processes[:5]:
        print(
            f"{process['name']} "
            f"(PID {process['pid']}) "
            f"- {process['memory']:.2f}% RAM"
        )

    time.sleep(2)