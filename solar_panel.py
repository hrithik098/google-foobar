# Google foobar solution 
def solution(area):
    ans=[]
    while(area>0):
        big = int(area**0.5)
        biggest = int(big**2)
        area-=biggest
        ans.append(biggest)
    return ans

t = int(input())
print(solution(t))

# n = int(input())
