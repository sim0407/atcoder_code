n,k=map(int,input().split())
p=[int(i) for i in input().split()]
p.sort()
ans=sum(p[0:k])
print(ans)