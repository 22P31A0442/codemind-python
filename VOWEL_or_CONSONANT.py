def sls(a):
    if a in 'aeiouAEIOU':
        return 'VOWEL'
    else:
        return 'CONSONANT'
a = input()
print(sls(a))