a = int(input())
if a<=199:
    p = 1.20
    b = a*p
    if b < 400:
        s=0
    else:
        s=b*15/100
    t = b+s;
elif a>=200 and a<400:
    p = 1.40
    b = a*p
    if b < 400:
        s=0
    else:
        s=b*15/100
    t = b+s;
elif a>=400 and a<600:
    p = 1.60
    b = a*p
    if b < 400:
        s=0
    else:
        s=b*15/100
    t = b+s;
elif a>=600 and a<800:
    p = 1.80
    b = a*p
    if b < 400:
        s=0
    else:
        s=b*15/100
    t = b+s;
else:
    p = 2.00
    b = a*p
    if b < 400:
        s=0
    else:
        s=b*15/100
    t = b+s;
    
print(f"Units Consumed: {a}")
print(f"Cost per Unit: {p:.2f}")
print(f"Bill: {b:.2f}")
print(f"Surcharge: {s:.2f}")
print(f"Total Amount: {t:.2f}")
    