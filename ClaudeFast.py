from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    print(f"Starting {name}")
    time.sleep(1)
    print(f"Finished {name}")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(task, f"Thread-{i}") for i in range(10)]

    print("All threads completed.")