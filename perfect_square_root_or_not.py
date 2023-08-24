x = int(input())
s=0
for i in range(1, x):
    if i*i==x:
        s=1
        break
if s==1:
    print("True")
else:
    print("False")