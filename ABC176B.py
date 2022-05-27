n=int(input())
tmp = 0
while n > 0:
    tmp += (n % 10)
    n = n // 10
if tmp % 9 == 0:
    ans = 'Yes'
else:
    ans ='No'
print(ans)

n=input()
n_arr = [int(n[i]) for i in range(len(n))]
tmp = 0
for i in n_arr:
    tmp += i
if tmp % 9 == 0:
    ans = 'Yes'
else:
    ans ='No'
print(ans)