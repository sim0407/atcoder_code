#input
n,m,x=map(int,input().split())
c=[]
for j in range(n):
    c.append([int(i) for i in input().split()])

#bit全探索 O(2**n*n*m<=2**12*12**2<10**6)
ans=-1
for i in range(2**n):
    und_list=[0]*m #理解度のリスト
    sum_money=0
    for j in range(n):
        if((i >> j)&1): #c[j]の参考書を選んでいるか
            for k in range(m): #それぞれのアルゴリズムについて
                und_list[k] += c[j][k+1]
            sum_money+=c[j][0]
    if min(und_list)>=x: #理解度がX以上になっているか
        if ans==-1:
            ans= sum_money
        elif ans > sum_money:
            ans=sum_money
print(ans)