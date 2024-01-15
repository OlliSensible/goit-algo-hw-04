import random
import timeit

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 
        L = arr[:mid]  
        R = arr[mid:]

        merge_sort(L) 
        merge_sort(R) 

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

def python_sort(arr):
    return sorted(arr)

def measure_time(func, array):
    start_time = timeit.default_timer()
    func(array)
    return timeit.default_timer() - start_time

test_data = [list(range(10000)), list(range(1000, 0, -1)), [random.randint(0, 10000) for _ in range(10000)]]

for arr in test_data:
    print(f"Merge Sort: {measure_time(merge_sort, arr.copy())} seconds")
    print(f"Insertion Sort: {measure_time(insertion_sort, arr.copy())} seconds")
    print(f"Python Sort (Timsort): {measure_time(python_sort, arr.copy())} seconds")