import numpy as np

rows = int(input("Enter number of rows :"))
columns = int(input("Enter number of columns :"))

print("Enter matrix elements row-wise : ")
elements = []
for i in range(rows):
    row = list(map(int , input().split()))
    elements.append(row)

matrix = np.array(elements)

print("\n Original matrix :")
print(matrix)

transpose = matrix.T
print("\n TRanspose matrix :")
print(transpose)
