import random
import threading
import time


class BaseThread(threading.Thread):
    """Base class for all threads"""

    __thread_count = 0

    def __init__(self, name="thread name not set"):
        """Constructor"""
        super().__init__()  # Use super() to call parent class constructor
        self.name = name
        BaseThread.__thread_count += 1
        print(f"Starting {self.name} created")

    def __del__(self):
        """Destructor"""
        BaseThread.__thread_count -= 1
        print(f"Ending {self.name} deleted")

    def get_thread_count(self):
        """Return thread count"""
        return BaseThread.__thread_count


class TestThread(BaseThread):
    """Child Class TestThread"""

    # Run thread
    def run(self):
        sleep_secs = random.randint(1, 4) + 1  # Simulate some variable workload...

        print(f"{self.name} -- Sleeping {sleep_secs} second(s) -- {self.get_thread_count()} thread(s)\n")
        time.sleep(sleep_secs)

        print(f"{self.name} -- {time.ctime(time.time())} -- {self.get_thread_count()} thread(s)\n")
        return


def test_threads():
    """Test Threads"""
    new_threads = []

    for i in range(0, 10):
        try:
            new_thread = TestThread(f"Thread-{i}")
            new_thread.start()
            new_threads.append(new_thread)

        except Exception as e:  # Use Exception instead of bare except
            print(f"*** Thread creation error iteration {i}: {e}")

    # Wait for all threads to complete
    for thread in new_threads:
        thread.join()

    return


# Main
print("\n\n—BOJ—\n\n")
test_threads()
print("\n\n—EOJ—\n\n")
