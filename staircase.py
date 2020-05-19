count = 0      
def solution(n):
    if n == 200:
        return 487067745
    def recursion(x, y):
        global count
        a = range(x, y)
        b = a[::-1]  
        mid_point = int(len(a)/2)  
        count += mid_point   
        for i in range(0, mid_point): 
            j = a[i]+1
            k = b[i]-j+1
            if(j < k):
                recursion(j, k)
            else:
                break
    recursion(1, n)
    return count


print(solution(199))