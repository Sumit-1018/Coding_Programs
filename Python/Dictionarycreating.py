import math
class computation():
        def fibonacci(self,n):
                if(n == 0):
                        return 0
                elif(n == 1):
                        return 1
                else:
                        return (fibonacci(n - 1) + fibonacci(n - 2))
        def factorial(self,n):
                return math.factorial(n)
obj=computation()
while True:
        try:
                n=int(input())
                break
        except ValueError:
                print("Enter valid integer")
print(f'''\n1. Factorial
2. Fibonacci''')
x=int(input("x:"))
if x==1:
        print(obj.factorial(n))
else:
        print(obj.fibonacci(n))