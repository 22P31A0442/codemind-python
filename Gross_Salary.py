s = int(input())
if s <= 10000:
    bs = s + (s*80/100)+(s*20/100)
    print(f"{bs:.2f}")
elif s <= 20000 and s >= 10000:
    bs = s+(s*90/100)+(s*25/100)
    print(f"{bs:.2f}")
else:
    bs = s+(s*95/100)+(s*30/100)
    print(f"{bs:.2f}")