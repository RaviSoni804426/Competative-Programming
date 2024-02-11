T=int(input())
for _ in range(T):
    X,Y=map(int,input().split())
    Z=(X*Y)%4
    if Z==0:
        print((X*Y)//4)
    else:
      print((X*Y)//4+1)
