# T=int(input())
# for _ in range(T):
#     X=int(input())
#     A=list(map(int,input().split()))
#     C=0
#     for i in range(X):
#      if A[i]>=1000:
#         C+=1
#         print(C) 
#      else:
#         print("0")
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    d = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if d[i] >= 1000:
            c += 1
    print(c)     
