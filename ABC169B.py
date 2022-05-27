n=int(input())
a=[int(i) for i in input().split()]
ans=1
for i in a:
    ans *= i
if ans > 10 ** 18:
    ans = -1
print(ans)


n=int(input())
a=[int(i) for i in input().split()]
ans=1
if 0 in a:
    ans = 0
else:
    for i in a:
        ans *= i
        if ans > 10 ** 18:
            ans = -1
            break
print(ans)