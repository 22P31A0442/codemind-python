p, r, t = map(int,input().split())
x = (1+r/100)**t
t = p*x
print(f"{t:.2f}")