# You have a RecentCounter class which counts the number of recent requests 
# within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in
# milliseconds, and returns the number of requests that has happened in the 
# past 3000 milliseconds (including the new request). Specifically, return the
# number of requests that have happened in the inclusive range [t - 3000, t].
#
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

 

# Solution 1:
# We create a simple object that tracks the most recent times in a queue and
# removes them as those calls become older than the desired time frame.

# Computational complexity: O(n) 
# Space complexity: O(n)

class RecentCounter:
    counter = 0
    time_frame = 3000
    recent = []

    def __init__(self):
        self.counter = 0        
        self.time_frame = 3000
        self.recent = []

    def ping(self, t: int) -> int:
        self.recent.append(t)
        self.counter += 1
        while self.recent[0] < t - self.time_frame:
            self.recent.pop(0)
            self.counter -= 1
            
        return self.counter