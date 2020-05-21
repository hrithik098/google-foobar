def solution(x,y):
    m,f  = int(x), int(y)
    count  = 0
    while not (m == 1 and f ==1):
        if f<=0 and m<=0:
            return str("impossible")
        elif f == 1:
            return str(count + m -1)
        else:
            count += int(m/f)
            m, f = f, m % f
    return str(count)