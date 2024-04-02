import random
import concurrent.futures
import time

def thread_task(name):
    """Function to be executed in a thread"""
    sleepSecs = random.randint(1, 4) + 1
    print(f"{name} -- Sleeping {sleepSecs} second(s)")
    time.sleep(sleepSecs)
    print(f"{name} -- Woke up at {time.ctime()}")

def testThreads():
    """Test Threads using ThreadPoolExecutor"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(thread_task, f"Thread-{ii}") for ii in range(10)]
        for future in concurrent.futures.as_completed(futures):
            future.result()

if __name__ == "__main__":
    print("\n\n—BOJ—\n\n")
    testThreads()
    print("\n\n—EOJ—\n\n")
