import time
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


arr = [17, 19, 24, 32, 41, 57, 62]
arr1 = [62, 57, 41, 32, 24, 19, 17]
arr2 = [17, 24, 41, 62, 19, 32, 57]
result = selection_sort(arr2)
print("output arr2")
start = time.time()
print(result)
end = time.time()

print("The time of execition of above program is : ", (end-start) * 10**3, "ms")
