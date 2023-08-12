y = int(input())
d = y%100
if d > 9:
    print(d)
else:
    print(f"0{d}")