def prime_sq(n):
  l=[]
  for i in range(2,n+1):

    for j in range(2,i):
      if (i%j)==0:
        break
    else:
      l.append(i**2)
      print(i)
  print(l)
n=int(input("n: "))
prime_sq(n)