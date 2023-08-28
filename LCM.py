a, b = map(int, input().split())
for i in range(1, a and b):
    if a%i==0 and b%i==0:
        g=i
lcm = a*b//g
print(lcm)