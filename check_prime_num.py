num = int(input(" Enter a number : "))
if num == 2:
    print("Prime")
elif num % 2 == 0 or num <= 1 :
    print("Not Prime")
else :
    i = 3
    while i * i <= num :
        if num % i == 0 :
            print("Not Prime")
            break
        i += 2
    else :
        print("Prime")