a = int(input())
if a<199:
    b =a*1.20
    if b<400:
        bb=b+100
    else:
        bb=b+b*15/100
    print(f"{bb:.2f}")
elif a >=200 and a<400:
    b = a*1.50
    if b<400:
        bb=b+100
    else:
        bb=b+b*15/100
    print(f"{bb:.2f}")
elif a >=400 and a<600:
    b = a*1.80
    if b<400:
        bb=b+100
    else:
        bb=b+b*15/100
    print(f"{bb:.2f}")
else:
    b = a*2.00
    if b<=400:
        bb=b+100
    else:
        bb=b+b*15/100
    print(f"{bb:.2f}")