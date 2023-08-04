from math import ceil

def power(n):
        a=0
        if n>0:
            for i in range(1,ceil(n/2)):
                print(i**3) 
                if (i**3)==n:
                    a+=1
                else:
                    pass
            if a>0:
                return True
            else:
                return False
        else:
            return False
n=int(input())
print(power(n))