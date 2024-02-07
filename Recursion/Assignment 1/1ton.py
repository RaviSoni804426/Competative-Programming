def number(n):
    if n==0:
        return
    for i in range(1,n+1):
        print(i)
        i+=1
n=int(input("Enter number: "))
print(number(n))
        