import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
variance = np.var(data)
correlation_matrix = np.corrcoef(data)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("Correlation Coefficients:")
print(correlation_matrix)
