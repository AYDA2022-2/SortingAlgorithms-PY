import time
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


arr = [17, 19, 24, 32, 41, 57, 62]
arr1 = [62, 57, 41, 32, 24, 19, 17]
arr2 = [17, 24, 41, 62, 19, 32, 57]
result = bubble_sort(arr2)
print("output arr2")
start = time.time()
print(result)
end = time.time()

print("The time of execition of above program is : ", (end-start) * 10**3, "ms")