import random
import time

# HeapSort implementation
def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# QuickSort implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    right = []
    left = []
    middle = []

    for item in arr:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        elif item == pivot:
            middle.append(item)
    return quick_sort(left) + middle + quick_sort(right)

# MergeSort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Timing function
def time_algorithm(algorithm, arr, inplace=False):
    arr_copy = arr.copy()  # Don't modify original
    start = time.time()
    if inplace:
        algorithm(arr_copy)
    else:
        algorithm(arr_copy)
    end = time.time()
    return end - start

# Test for different input sizes and distributions
sizes = [1000, 5000, 10000, 20000]
distributions = {
    "random": lambda n: [random.randint(0, 100000) for _ in range(n)],
    "sorted": lambda n: list(range(n)),
    "reverse": lambda n: list(range(n, 0, -1))
}

# Running experiments
for dist_name, dist_func in distributions.items():
    print(f"\n--- Distribution: {dist_name} ---")
    for n in sizes:
        arr = dist_func(n)

        t_heap = time_algorithm(heap_sort, arr, inplace=True)
        t_quick = time_algorithm(quick_sort, arr)
        t_merge = time_algorithm(merge_sort, arr)

        print(f"Size {n}: HeapSort={t_heap:.5f}s, QuickSort={t_quick:.5f}s, MergeSort={t_merge:.5f}s")
