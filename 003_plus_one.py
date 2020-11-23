def plus_one_1(arr):
    r = 1
    res = []
    for i in reversed(arr):
        r_ = (i + r) // 10
        i = (i + r) % 10
        r = r_
        res.append(i)
    if r > 0:
        res.append(r)
    return list(reversed(res))


def plus_one_2(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

# My optimal solution
def plus_one_3(A):
    r = 1
    for i in reversed(range(len(A))):
        r_ = (A[i] + r) // 10
        A[i] = (A[i] +r) % 10
        r = r_
        if r == 0:
            break
    if r > 0:
        A.insert(0, r)
    return A

def plus_one_4(A):
    r = 1
    for i in reversed(range(len(A))):
        r  = (A[i] + r)
        if r > 9:
            r = 1
            A[i] = 0
        else:
            A[i] = r
            r = 0
            break
    if r > 0:
        A.insert(0, r)
    return A

if __name__ == "__main__":
    plus_one_3([9, 7, 9, 9]) 
