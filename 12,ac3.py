num=int(input("Enter a numer: "))
s=str(num)
n=len(s)
if n%2==1:
    product=int(s[n//2])
else:
    mid1=int(s[n//2-1])
    mid2=int(s[n//2])
    product=mid1*mid2
print("Product of middle digit(s) is: ",product)