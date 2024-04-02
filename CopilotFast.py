import random
import threading
import time

class TestThread (threading.Thread):
    '''Child Class TestThread'''
    threadCount = 0

    def __init__ (self, name = "thread name not set"):
        """Constructor"""
        threading.Thread.__init__(self)
        self.name = name
        TestThread.threadCount += 1
        print (f"Starting {self.name} created")

    #  Run thread
    def run (self):
        sleepSecs = random.randint(1, 4) + 1  # Simulate some variable workload...
        print (f"{self.name} -- Sleeping {sleepSecs} second(s) -- {TestThread.threadCount} thread(s)\n")
        time.sleep (sleepSecs)
        print (f"{self.name} -- {time.ctime (time.time())} -- {TestThread.threadCount} thread(s)\n")
        TestThread.threadCount -= 1
        return

def testThreads ():
    '''Test Threads'''
    newThreads = [TestThread (f"Thread-{ii}") for ii in range (10)]
    for newThread in newThreads:
        newThread.start()

    # Wait for all threads to complete
    for tt in newThreads:
       tt.join ()

    return

# Main
print ("\n\n—BOJ—\n\n")
testThreads ()
print ("\n\n—EOJ—\n\n")
