n=int(input())
m=int(input())

def kaprekar(n,m):
    return [i for i in range(n,m+1) if check(i)]
def check(i):
    sq=str(i**2)
    le=len(str(i))
    r=sq[-le:]
    l=sq[:-le] or "0"
    return sum(map(int,(l,r)))==i

print(*kaprekar(n,m) or ["INVALID RANGE"])
