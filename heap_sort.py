arr = [4, 10, 3, 5, 11, 23, 1]
n = len(arr)

def heapify(arr, n, i):
  largest = i  
  left = 2 * i + 1  
  right = 2 * i + 2    

  #compare left child node with the parent node
  if left < n and arr[left] > arr[largest]:
    largest = left

  #compare right child node with the parent node
  if right < n and arr[right] > arr[largest]:
    largest = right
  
  #check if the current largest is the the current i node
  if i != largest:
    #swap the position for i and current largest
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)

    
for i in range(n//2 -1 , -1, -1):
    heapify(arr, n, i)

print ("Original Array:", arr)
print("Max Heap:", arr)

