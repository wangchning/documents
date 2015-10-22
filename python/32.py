#!/usr/bin/env python3
for i in range(1,100):
    p,j=0,i
    while i!=1:
        if i%2==0:
            i/=2
        else:
            i=i*3+1
        p+=1
    print([j,p])
