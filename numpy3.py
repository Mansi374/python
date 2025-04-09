import numpy as np
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("1D Array:")
print(arr_1d)
print("\n2D Array:")
print(arr_2d)
print("\n3D Array:")
print(arr_3d)

reshaped = arr_1d.reshape(5, 1)
print("\nReshaped 1D Array to 2D:")
print(reshaped)
print("\nElement at position (1,2) in 2D array:", arr_2d[1, 2])
print("\nFirst row of 2D array:")
print(arr_2d[0, :])
