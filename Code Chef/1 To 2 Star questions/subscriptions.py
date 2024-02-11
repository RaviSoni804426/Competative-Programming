T=int(input())
for _ in range(T):
  N,X=map(int,input().split())
  if N<=6:
    print(int(X))
  elif N>6:
    if N%6==0:
      print(int(N/6*X))
    else:
      print((int(N/6+1)*X))
  
 