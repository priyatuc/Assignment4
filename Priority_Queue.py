# Task Class Definition
class Task:
    def __init__(self, task_id, priority, deadline, arrival_time):
        self.task_id = task_id
        self.priority = priority
        self.deadline = deadline
        self.arrival_time = arrival_time

# Sample Tasks
task1 = Task(task_id=1, priority=5, deadline="2023-12-01", arrival_time="2023-11-01")
task2 = Task(task_id=2, priority=8, deadline="2023-11-15", arrival_time="2023-11-05")
task3 = Task(task_id=3, priority=3, deadline="2023-12-10", arrival_time="2023-11-10")

list_of_tasks = [task1, task2, task3]
n = len(list_of_tasks)

# Heapify Function (Max-Heap)
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Compare left child
    if left < n and arr[left].priority > arr[largest].priority:
        largest = left

    # Compare right child
    if right < n and arr[right].priority > arr[largest].priority:
        largest = right

    # Swap and recurse if needed
    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Build Initial Heap
for i in range(n // 2 - 1, -1, -1):
    heapify(list_of_tasks, n, i)

# Insert Function
def insert(heap, task):
    # Insert a new task into the heap and maintain the heap property.
    heap.append(task)
    i = len(heap) - 1

    # Bubble up to maintain max-heap property
    while i > 0:
        parent = (i - 1) // 2
        if heap[i].priority > heap[parent].priority:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

# Extract Max Function
def extract_max(heap):
    # Remove and return the task with the highest priority.
    if len(heap) == 0:
        return None

    root_task = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    heapify(heap, len(heap), 0)
    return root_task

# Increase Key Function
def increase_key(heap, task_index, new_priority):
    # Increase the priority of a task and bubble it up if necessary.
    if new_priority < heap[task_index].priority:
        print("New priority is lower than current — use decrease_key instead.")
        return

    heap[task_index].priority = new_priority

    # Bubble up
    while task_index > 0:
        parent = (task_index - 1) // 2
        if heap[task_index].priority > heap[parent].priority:
            heap[task_index], heap[parent] = heap[parent], heap[task_index]
            task_index = parent
        else:
            break

# Is Empty Function
def is_empty(heap):
    # Check if the heap is empty.
    return len(heap) == 0

# Example Usage
if __name__ == "__main__":
    # Insert a new task
    task4 = Task(task_id=4, priority=10, deadline="2023-12-20", arrival_time="2023-11-15")
    insert(list_of_tasks, task4)

    # Increase priority of an existing task
    increase_key(list_of_tasks, 2, 12)

    # Extract tasks by priority
    print("Extracting tasks in order of priority:")
    while not is_empty(list_of_tasks):
        t = extract_max(list_of_tasks)
        print(f"Task ID: {t.task_id}, Priority: {t.priority}, Deadline: {t.deadline}, Arrival Time: {t.arrival_time}")
