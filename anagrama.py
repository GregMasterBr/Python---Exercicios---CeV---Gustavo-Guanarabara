def perm(s, i=0):
    if i == len(s) - 1:
        print(s)
    else:
        for j in range(i, len(s)):
            t = s
            s = s[j] + s[:j] + s[(j + 1):]
            perm(s, i + 1)
            s = t
perm('AB')

