T=int(input())
for _ in range(T):
    X,Y,Z=map(int,input().split())
    if (X+Y)and (Y+Z)and (Z+X)and (X+Y+Z)>1:
        print("Not Now")
    else:
        print("Water filling time")
