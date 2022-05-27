n=int(input())
a=[int(i) for i in input().split()]

maximum = 0
step_sum = 0
for i in a:
    maximum = max(maximum, i)
    step_sum += maximum - i
print(step_sum)