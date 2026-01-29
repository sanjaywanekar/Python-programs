L1 = list(map(int , input("Enter first list : ").split()))
L2 = list(map(int , input("Enter second list : ").split()))
common = list(set(L1) & set(L2))
print("common elements are :" , common)
