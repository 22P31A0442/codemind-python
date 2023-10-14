a, b, c = map(int, input().split())
cap = 2*a*b*c*512
print(f"{cap//1024}KB")