import concurrent.futures
import random
import time

class OptimizedThread:
    def __init__(self, name):
        self.name = name

    def run(self):
        sleep_time = random.randint(1, 4) + 1
        print(f"{self.name} -- Sleeping {sleep_time} second(s)")
        time.sleep(sleep_time)
        print(f"{self.name} -- Done")

def optimized_test_threads():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(OptimizedThread(f"Thread-{i}").run) for i in range(10)]
        concurrent.futures.wait(futures)  # Wait for all threads to complete

if __name__ == "__main__":
    print("\n\n—BOJ—\n\n")
    optimized_test_threads()
    print("\n\n—EOJ—\n\n")
