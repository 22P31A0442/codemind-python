def sls(n):
    if n>=90:
        return 'Grade A'
    elif n>=80 and n<90:
        return 'Grade B'
    elif n>=70 and n<80:
        return 'Grade C'
    elif n>=60 and n<70:
        return 'Grade D'
    elif n>=40 and n<60:
        return 'Grade E'
    else:
        return 'Grade F'
a, b, c, d, e = map(int,input().split())
n = (a+b+c+d+e)//5
print(sls(n))