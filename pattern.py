rows = int(input("Enter the number of rows: "))

# Loop to print the pattern
for i in range(1, rows + 1):
    print(" "*(rows-i)+"*" * (i))
