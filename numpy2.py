import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

addition = arr1 + arr2
subtraction = arr1 - arr2
multiplication = arr1 * arr2
division = arr1 / arr2

print("Element-wise Addition:")
print(addition)
print("\nElement-wise Subtraction:")
print(subtraction)
print("\nElement-wise Multiplication:")
print(multiplication)
print("\nElement-wise Division:")
print(division)
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
dot_product = np.dot(vec1, vec2)
cross_product = np.cross(vec1, vec2)

print("\nDot Product of vectors:", dot_product)
print("Cross Product of vectors:", cross_product)
