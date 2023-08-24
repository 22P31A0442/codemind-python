a, b, c = map(int, input().split())
ci = a * ((1+(b/100))**c)
print(f"{ci:.2f}")