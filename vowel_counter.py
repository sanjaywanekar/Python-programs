string = input("Enter a string : ").lower()
vowels = 'aeiou'
count = 0 
for ch in string :
    if ch in vowels :
        count += 1
print("Number of vowels :" , count )
