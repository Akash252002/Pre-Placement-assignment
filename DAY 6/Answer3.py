def searchMatrix(self, a, target):
    n = len(a)
    m = len(a[0])
    i = 0
    j = m - 1
    while i < n and j >= 0:
        if target == a[i][j]:
            return True
        if target > a[i][j]:
            i += 1
        else:
            j -= 1
    return False