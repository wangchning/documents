#! /usr/bin/env python3
import gmpy2 as gp
def fsst(x):
  try:
    x=gp.mpz(x)
  except TypeError:
    print("参数必须是整数")
  t=[]
  p=1
  while x!=1:
    p=gp.next_prime(p)
    while x%p==0:
      t.append(p)
      x//=p
  t=list(map(abcd,t))
  while len(t)>1:
    a,b,c,d=t.pop(0)
    w,x,y,z=t.pop(0)
    t.append((a*w+b*x+c*y+d*z,a*x-b*w-c*z+d*y,a*y+b*z-c*w-d*x,a*z-b*y+c*x-d*w))
  a,b,c,d=t[0]
  return a,b,c,d

def abcd(p):
  if p==2:
    return (1,1,0,0)
  s=[x*x for x in range((p+1)//2)]+[-x*x-1 for x in range((p+1)//2)]
  s=[x%p for x in s]
  for i in s:
    if s.count(i)==2:
      k=i
      break
  k1=s.index(k)
  s[k1]=p
  k2=s.index(k)-((p+1)//2)
  return (k1,k2,1,0)

print(fsst(7))
