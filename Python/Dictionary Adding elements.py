def marvel(i,j,k):
  c=0
  for x in range(i,j+1):
    if (x+(int(str(x)[::-1])))%k==0:
      c+=1
    else:
      break
  print(c)
a=map(int,input().split(" "))
a=[i for i in a]
i=a[0]
j=a[1]
k=a[2]
marvel(i,j,k)