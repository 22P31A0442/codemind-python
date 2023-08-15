a, b, c = map(int, input().split())
s=(a+b+c)/2
area = s*(s-a)*(s-b)*(s-c)
x = area ** 0.5
print(f"{x:.2f}")