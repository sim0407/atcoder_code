n=int(input())
a=[int(i) for i in input().split()]
a.sort()
q=int(input())
bc=[]
for i in range(q):
    bc.append([int(i) for i in input().split()])

for i in bc:
    a = [i[1] if j == i[0] else j for j in a]
    print(sum(a))

#[真の値 if 条件式 else 偽の値 for 任意の変数名 in 元のリスト]6b



n=int(input())
a=[int(i) for i in input().split()]
a.sort()
q=int(input())
bc=[]
for i in range(q):
    bc.append([int(i) for i in input().split()])

import collections
collect = collections.Counter(a)
#print(collect)

for i in bc:
    #if i[0] in collect:
    if i[1] in collect:
        collect[i[1]] += collect.pop(i[0],0)
    else:
        if i[0] in collect:
            collect[i[1]] = collect.pop(i[0],0)
    ans=0
    for k,v in collect.iteritems():
        ans += (k * v)
    print(ans)
    


#sum を計算しておく
n=int(input())
a=[int(i) for i in input().split()]
a.sort()
q=int(input())
bc=[]
for i in range(q):
    bc.append([int(i) for i in input().split()])

import collections
collect = collections.Counter(a)

ans=0
for k,v in collect.items():
    ans += (k * v)
for i in bc:
    if i[0] in collect:
        if i[1] in collect:
            ans += ((i[1]-i[0]) * collect[i[0]])
            collect[i[1]] += collect.pop(i[0],0)
        else:
            ans += ((i[1]-i[0]) * collect[i[0]])
            collect[i[1]] = collect.pop(i[0],0)
    print(ans)