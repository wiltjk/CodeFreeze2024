'''BadThreads Sample Code'''
import random
import threading
import time

class BaseThread (threading.Thread):
    '''Base class for all Threads'''
    __threadCount = 0
    

    def __init__ (self, name = "thread name not set"):
        """Constructor"""
        threading.Thread.__init__(self)
        self.name = name
        BaseThread.__threadCount += 1
        print (f"Starting {self.name} created")
                

    def __del__ (self):
        '''Destructor'''
        BaseThread.__threadCount -= 1
        print (f"Ending {self.name} deleted")
        

    def getThreadCount (self):
        '''Return thread count'''
        return BaseThread.__threadCount
        
        
        
class TestThread (BaseThread):
    '''Child Class TestThread'''
    #  Run thread
    def run (self):
        sleepSecs = random.randint(1, 4) + 1  # Simulate some variable workload...
        
        print (f"{self.name} -- Sleeping {sleepSecs} second(s) -- {self.getThreadCount ()} thread(s)\n")
        time.sleep (sleepSecs)
        
        print (f"{self.name} -- {time.ctime (time.time())} -- {self.getThreadCount ()} thread(s)\n")
        return
        
        

def testThreads ():
    '''Test Threads'''
    newThreads = []
        
    for ii in range (0, 10):
        try:
            newThread = TestThread (f"Thread-{ii}")
            newThread.start ()
            newThreads.append (newThread)
            
        except:
            print (f"*** Thread creation error iteration {ii}.") 
    
    # Wait for all threads to complete
    for tt in newThreads:
       tt.join ()
   
    return


# Main
print ("\n\n—BOJ—\n\n")
testThreads ()
print ("\n\n—EOJ—\n\n")