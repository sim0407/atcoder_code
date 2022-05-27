#after contest
n=int(input())
a=[int(i) for i in input().split()]
all_xor = 0
for i in a:
    all_xor ^= i
for i in a:
    print(i ^ all_xor , end=' ')
