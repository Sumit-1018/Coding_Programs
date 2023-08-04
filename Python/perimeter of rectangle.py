def factorial(n):
  if n==1:
    return(1)
  else:
    return(n*factorial(n-1))
def sum(n,x):
  total=1.0
  for i in range(1,x+1,1):
    total=total+(pow(n,2)/factorial(i))
  return(total)
if __name__=='__main__':
  n=int(input("n: "))
  x=int(input("x: "))
  print('%.2f'%(sum(x,n)))