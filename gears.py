from fractions import Fraction
def answer(pegs):
    l = len(pegs)
    j = 0
    for i in range(1,l):
        j=pegs[i] -(pegs[i-1]+j)  
    k = j
    if len(pegs)%2 == 0:
        if k >= 3/2:
            x = Fraction(k*2, 3)
            a = x.numerator/x.denominator 
            for i in range(0, len(pegs)-2): 
                b = pegs[i+1]-pegs[i]
                if a < 0 or a > b-1:
                    return [-1, -1]
                a = b - a
            return [x.numerator, x.denominator]
        else:
            return [-1, -1]
    else:
        if k <= -1/2:
            x = Fraction(k*(-2), 1)
            a = x.numerator/x.denominator 
            for i in range(0, len(pegs)-2): 
                b = pegs[i+1]-pegs[i]
                if a < 0 or a > b-1:
                    return [-1, -1]
                a = b - a
            return [x.numerator, x.denominator]
        else:
            return [-1, -1]

print(answer([4, 30, 50]))
