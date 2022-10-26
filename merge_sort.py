import time
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array


arr = [17, 19, 24, 32, 41, 57, 62]
arr1 = [62, 57, 41, 32, 24, 19, 17]
arr2 = [17, 24, 41, 62, 19, 32, 57]
result = merge_sort(arr2)
print("output arr2")
start = time.time()
print(result)
end = time.time()

print("The time of execition of above program is : ", (end-start) * 10**3, "ms")
