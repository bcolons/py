from collections import deque
tasks = deque()
def task1(): print("Task 1")
def task2(): print("Task 2")


#cant execute concurrently
"""
def countup(n):
    for i in range(n):
        print(f"Printing {i}")
def countdown(n):
    for i in range(n):
        print(f"Printing {n - i}")
"""
def countup(n):
    print(f"Printing countup {n}")
    tasks.append(lambda: countup(n-1))
def countdown(n):
    def _run(i):
        print(f"Printing countdown {n}.{i}")
        tasks.append(lambda: _run(n-1))
    _run(n-1)

#main
tasks.append(task1)
tasks.append(task2)
tasks.append(lambda: countup(5))
tasks.append(lambda: countdown(5))

while tasks:
    task = tasks.popleft()
    task()
