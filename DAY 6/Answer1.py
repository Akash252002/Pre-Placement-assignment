
def diStringMatch(self, s):
    n = len(s)
    x, y = 0, n
    v = []
    for i in range(n):
        if s[i] == 'I':
            v.append(x)
            x += 1
        else:
            v.append(y)
            y -= 1
    v.append(x)
    return v
