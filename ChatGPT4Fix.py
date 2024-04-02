import random
import threading
import time

class BaseThread(threading.Thread):
    """Base class for all Threads"""
    __threadCount = 0
    __threadLock = threading.Lock()

    def __init__(self, name="thread name not set"):
        """Constructor"""
        threading.Thread.__init__(self)
        self.name = name
        with BaseThread.__threadLock:
            BaseThread.__threadCount += 1
        print(f"Starting {self.name} created")

    @classmethod
    def getThreadCount(cls):
        """Return thread count"""
        with cls.__threadLock:
            return cls.__threadCount

class TestThread(BaseThread):
    """Child Class TestThread"""
    def run(self):
        sleepSecs = random.randint(1, 4) + 1
        print(f"{self.name} -- Sleeping {sleepSecs} second(s) -- {self.getThreadCount()} thread(s)\n")
        time.sleep(sleepSecs)
        print(f"{self.name} -- {time.ctime(time.time())} -- {self.getThreadCount()} thread(s)\n")

def testThreads():
    """Test Threads"""
    newThreads = []
    for ii in range(10):
        try:
            newThread = TestThread(f"Thread-{ii}")
            newThread.start()
            newThreads.append(newThread)
        except Exception as e:
            print(f"*** Thread creation error iteration {ii}: {e}")
    for tt in newThreads:
        tt.join()

if __name__ == "__main__":
    print("\n\n—BOJ—\n\n")
    testThreads()
    print("\n\n—EOJ—\n\n")
