x = int(input())
max=0
while x!=0:
    r = x%10
    x=x//10
    if r>max:
        max=r
print(max)