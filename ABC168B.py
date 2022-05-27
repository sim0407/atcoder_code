k=int(input())
s=input()
if len(s)<=k:
    ans=s
else:
    ans=s[0:k]+"..."
print(ans)