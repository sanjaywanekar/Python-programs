rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of columns : "))

print("\n Enter elements of first matrix :")
A = []
for i in range (rows):
    row = list(map(int , input(). split()))
    A.append(row)

print("\n Enter elements of second matrix : ")
B = []
for i in range (rows) :
    row = list(map(int , input() . split()))
    B.append(row)


result = []
for i in range (rows) :
    row = []
    for j in range (cols):
        row.append(A[i][j] + B[i][j])
    result.append (row)

print("\n Resultant matrix after addition : ")
for i in range (rows) :
    for j in range (cols):
        print(result[i][j] , end = " ")

    print()
