import time
arr = [17, 19, 24, 32, 41, 57, 62]
arr1 = [62, 57, 41, 32, 24, 19, 17]
arr2 = [17, 24, 41, 62, 19, 32, 57]


print("output arr")
arr.sort()
start = time.time()
print(arr)
end = time.time()
print("The time of execition of above program is : ", (end-start) * 10**3, "ms")

print("output arr1")
arr1.sort()
start = time.time()
print(arr1)
end = time.time()
print("The time of execition of above program is : ", (end-start) * 10**3, "ms")

print("output arr2")
arr2.sort()
start = time.time()
print(arr2)
end = time.time()
print("The time of execition of above program is : ", (end-start) * 10**3, "ms")
