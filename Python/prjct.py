import random

while True:
    try:
        a=int(input("Enter the lower range:"))
        break
    except ValueError:
        print("This is not a valid input. Please enter an integer!")
        print()

while True:
    try:
        b=int(input("Enter the upper range:"))
        break
    except ValueError:
        print("This is not a valid input. Please enter an integer!")
        print()
        
if a>b:
    number=random.randint(b,a)
    print("The range is ("+str(b)+","+str(a)+") and randomly picked number is",number)
else:
    number=random.randint(a,b)
    print("The range is ("+str(a)+","+str(b)+") and randomly picked number is",number)

print("The properties followed by this number are:")

if number>0:
    print(number,"is a positive number")
elif number==0:
    print(number,"is neither positive nor negative")
else:
    print(number,"is a negative number")

if number%2==0:
    print(number,"is an even number")
else:
    print(number,"is an odd number")

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is NOT a prime number")
            break
    else:
        print(number, "is a PRIME number")
elif number == 0 or number == 1:
    print(number, "is neither prime nor composite number")
else:
    print(number, "is negative number which is neither prime nor composite")
