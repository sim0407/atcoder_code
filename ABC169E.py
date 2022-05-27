n=int(input())
a=[]
b=[]
for i in range(n):
    tmp = input().split()
    a.append(int(tmp[0]))
    b.append(int(tmp[1]))
a_sorted = sorted(a)
b_sorted = sorted(b)

if n % 2 == 1:
    ans = b_sorted[(n-1)//2] - a_sorted[(n-1)//2] + 1
else:
    ans = (b_sorted[n//2-1] + b_sorted[n//2]) - (a_sorted[n//2-1] + a_sorted[n//2]) + 1
print(ans)