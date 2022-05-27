x,n=map(int,input().split())
if n == 0:
    print(x)
else:
    p=set([int(i) for i in input().split()])
    for i in range(1000):
        if not(x-i in p):
            ans=x-i
            break
        elif not(x+i in p):
            ans=x+i
            break
    print(ans)