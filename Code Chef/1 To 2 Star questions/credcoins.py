T=int(input())
for _ in range(T):
    X,Y=map(int,input().split())
    Z=(X*Y)%100
    if Z==0:
        print(X*Y//100)
    elif Z!=0:
        print((X*Y//100-1)+1)