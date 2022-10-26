import time
def shell_sort(array):
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array


arr = [17, 19, 24, 32, 41, 57, 62]
arr1 = [62, 57, 41, 32, 24, 19, 17]
arr2 = [17, 24, 41, 62, 19, 32, 57]
result = shell_sort(arr2)
print("output arr2")
start = time.time()
print(result)
end = time.time()

print("The time of execition of above program is : ", (end-start) * 10**3, "ms")