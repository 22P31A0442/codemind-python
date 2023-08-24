a, b, c = map(int, input().split())
i = (1+(b/100))**c
ci = a*i
print(f"{ci:.2f}")