import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

# print the type of numpy array
print(type(arr))

print(arr.max())
print(arr.min())
print(arr.mean())

print("before sorting", arr)
arr.sort()
print("after sorting", arr)


#Reverse the array using np.flip
reversed_array = np.flip(arr)

print("Original array:", arr)
print("Reversed array:", reversed_array)

