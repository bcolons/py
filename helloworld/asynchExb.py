#not wokring
import time
from collections import deque
tasks = deque()
sleeping = []
def countup(n):
    print(f"Printing countup {n}")
    sch_task( lambda: countup(n+1), 3)
def countdown(n):
    print(f"Printing countdown {n}")
    sch_task( lambda: countdown(n-1), 2)
def sch_task(task, delay):
    deadline = time.time() + delay # in s
    sleeping.append((deadline,task))
    for asleep in sleeping:
        if time.time() > asleep[0] :
            tasks.append(asleep[1])
#main
sch_task(countup(5),3)
sch_task(countdown(5),2)

while tasks:
    task = tasks.popleft()
    task()
