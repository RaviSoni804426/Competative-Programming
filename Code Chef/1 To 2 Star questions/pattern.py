n=5

for i in range(5):
 for j in range(5):
  if (j<=i)or(j>=n-1-i):
   print("*",end="")
  else:
   print(" ",end="")
print()
  