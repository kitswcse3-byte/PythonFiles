def rev(x):
    r=0
    while(x>0):
        num=x%10
        r=r*10+num
        x//=10
    return r

a = int(input())
print(rev(a))


