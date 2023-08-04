def remove(str1,ind):
    if ind<len(str1):
        a=str1[:ind+1:]+str1[ind+2::]
        if a=="":
            return("Empty")
        else:
            return(a)
    else:
        return("Index out of range")
str1=str(input())
ind=int(input())
print(remove(str1,ind))