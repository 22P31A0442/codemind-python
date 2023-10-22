a = list(map(int, input().split()))
flag=0
for i in a:
    if i<=34:
        flag=1
if flag==1:
    print("FAILED")
else:
    print("PASSED")