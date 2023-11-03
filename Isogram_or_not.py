s = input()
x=0
for i in s:
    if s.count(i)>1:
        x=x+1
        print("False")
        break
if x==0:
    print("True")