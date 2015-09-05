#! /usr/bin/env python3
def re(f):
  n=len(f)
  for i in range(1,2*n-1,2):
    f[i:i]=[(f[i-1][0]+f[i][0],f[i-1][1]+f[i][1])]
  return f

def farui_first(n):
  if n==1:
    return [(0,1),(1,1)]
  return re(farui_first(n-1))

def farui(n):
  f1=farui_first(n)
  for i in range(len(f1)):
    if f1[i][1]>n:
      f1[i]=0
  f=[]
  [f.append(a) for a in f1 if not a in f]
  if 0 in f:
    f.remove(0)
  return f
print(farui(16))
