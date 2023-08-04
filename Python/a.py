a=map(int,input().split(","))
a=[i for i in a]
try:
  b=int(input())
  print(a[b])
except:
  print(len(a)/sum(a))
finally:
  print("Error Handled")