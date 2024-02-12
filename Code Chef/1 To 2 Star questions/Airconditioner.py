T=int(input())
for _ in range(T):
    A,B,C=map(int,input().split())
    if B>=C and B>=A:
        print("Yes")
    else:
        print("No")  