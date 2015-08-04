#! /usr/bin/env python3.4
def ddd(n):
  """此函数用于解决前n位数被n整除的问题"""
  if n==1:
    return list(range(1,10))
  else:
    s=[]
    t=ddd(n-1)
    for i in t:
      for j in range(1,10):
        if (i*10+j)%n==0 and (str(j) not in set(str(i))):
          s.append(i*10+j)
    return s

print(ddd(9))
