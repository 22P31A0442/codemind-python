n = int(input())
list1 = list(map(int, input().split()))
s=0
for i in range(0,n):
    if list1[i]%2!=0:
        s=i
print(s)