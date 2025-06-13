def kth_largest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)

def kth_largest(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n-k]


import heapq

def kth_largest(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k - 1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)

arr = [3, 1, 5, 12, 2, 11]
k = 3
result = kth_largest(arr, k)
print(f"The {k}rd largest element in {arr} is {result}")