def solution(start, length):
    xor = 0
    a = start
    b= length
    while b > 0:
        xor ^= check(a) + check(a+b)
        a += length
        b -=1
    return xor

def check(m):
    if m == 0:
        return 0
    if (m-1)%4 == 0:
        return m-1
    elif (m-1)%4 ==1:
        return 1
    elif (m-1)  % 4 ==2:
        return m
    else:
        return 0 
