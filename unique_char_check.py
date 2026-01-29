def has_unique_char(s):
    return len(s)==len(set(s))
# here we defined a function called has_unique_char which holds a string as 's' 
# and in te 2nd step we put the string in set so it removes all the duplicate characters of the string , after that we compare the length of original string and the string we stored in the set .
# if the lenght of both the string id equal than all the characters are unique and if length is not equal thain characters are not unique


string = input("Enter a string :")
if has_unique_char(string):
    print("All characters are unique.")
else:
    print("characters are not unique")