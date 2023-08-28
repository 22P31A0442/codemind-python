x = int(input())
s=0
while x!=0:
    r=x%10
    s=s+1
    x=x//10
if s==10:
    print("Valid")
else:
    print("Invalid")