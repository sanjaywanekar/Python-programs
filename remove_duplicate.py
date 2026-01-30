List = [1,2,2,3,4,4,4,5,5]
result = []
for x in List :
    if x not in result :
        result.append(x)

print(" Original list : " , List)
print("List after removing duplicates : " , result )