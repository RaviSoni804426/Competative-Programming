# n=int(input("Enter test cases: "))
# for i in range(1,n+1):
#     a,b,c=map(int(input()))
#     average=(a+b)/2
#     if average>c:
#         print("YES")
#     else:
#         print("NO")
T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    average = (A + B) / 2
    if average > C:
        print("YES")
    else:
        print("NO")