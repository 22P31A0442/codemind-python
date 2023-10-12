n = int(input())
list1 = list(map(int, input().split()))
x=int(input())
s=0
for i in list1:
    if x==i:
        s=s+1
print(s)