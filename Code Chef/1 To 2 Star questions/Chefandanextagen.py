T=int(input())
for _ in range(T):
 X,Y,Z,A=map(int,input().split())
 if (X*Y)>(Z*A):
        print("No")
 else:
        print("Yes")