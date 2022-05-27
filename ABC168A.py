n=int(input())
_mod = n%10
if _mod == 3:
    ans="bon"
elif _mod == 0 or _mod == 1 or _mod == 6 or _mod == 8:
    ans="pon"
else:
    ans="hon"
print(ans)