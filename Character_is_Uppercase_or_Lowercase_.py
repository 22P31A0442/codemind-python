def sls(c):
    if ord(c)>=65 and ord(c)<=92:
        return 'uppercase alphabet'
    elif ord(c)>=97 and ord(c)<=122:
        return 'lowercase alphabet'
    else:
        return 'not an alphabet'
c = input()
print(sls(c))