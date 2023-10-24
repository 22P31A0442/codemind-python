def sls1(n):
    print(f"{(n+(n*0.8)+(n*0.2)):.2f}")
def sls2(n):
    print(f"{(n+(n*0.90)+(n*0.25)):.2f}")
def sls3(n):
    print(f"{(n+(n*0.95)+(n*0.3)):.2f}")
n = int(input())
if n<=10000:
    sls1(n)
elif n>10000 and n<=20000:
    sls2(n)
else:
    sls3(n)