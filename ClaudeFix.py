'''Improved Threads Sample Code'''

import random
import threading
import time

class BaseThread(threading.Thread):
    '''Base class for all Threads'''
    
    thread_count = 0

    def __init__(self, name="thread name not set"):
        """Constructor"""
        threading.Thread.__init__(self) 
        self.name = name
        BaseThread.thread_count += 1
        print(f"Starting {self.name} created")

    def __del__(self):
        '''Destructor'''
        BaseThread.thread_count -= 1
        print(f"Ending {self.name} deleted")

    def get_thread_count(self):
        '''Return thread count'''
        return BaseThread.thread_count
        

class TestThread(BaseThread):
    '''Child Class TestThread'''
    
    def __init__(self, name):
        super().__init__(name)
        
    # Run thread
    def run(self):
        sleep_secs = random.randint(1, 4) + 1  # Simulate variable workload
        
        print(f"{self.name} -- Sleeping {sleep_secs} second(s) -- {self.get_thread_count()} thread(s)")
        time.sleep(sleep_secs)
        
        print(f"{self.name} -- {time.ctime(time.time())} -- {self.get_thread_count()} thread(s)")
        
      
def test_threads():
    '''Test Threads'''
        
    threads = []
    
    for i in range(10):
        try:
            thread = TestThread(f"Thread-{i}")
            thread.start()
            threads.append(thread)
        except:
            print(f"*** Thread creation error on iteration {i}.")
            
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
        
if __name__ == "__main__":
    print("\nStarting threads...")
    test_threads()
    print("All threads completed.")