def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n=int(input("Enter a: "))
m=int(input("Enter b: "))
result = gcd(n, m)
print(result)

