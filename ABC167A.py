s=input()
t=input()

ans="Yes"

if len(s)+1 != len(t):
    ans = "No"
elif s != t[0:-2]:
    ans="No"
print(ans)
