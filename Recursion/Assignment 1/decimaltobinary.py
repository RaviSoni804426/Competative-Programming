def decimaltobinary(n):
    if n==0:
        return 
    decimaltobinary(n//2)
    print(n%2,end="")
n=int(input("Enter number: "))
print(decimaltobinary(n))