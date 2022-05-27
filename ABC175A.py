s=input()
cnt=0
_max=0
for i in [s[0],s[1],s[2]]:
    if i == 'R':
        cnt += 1
        if _max < cnt:
            _max = cnt
    else:
        cnt = 0
print(_max)