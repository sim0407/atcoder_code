x,y=map(int,input().split())
Low=2*x
High=4*x
ans='No'
if y % 2 == 0:
    if y>=Low and y<=High:
        ans='Yes'
print(ans)