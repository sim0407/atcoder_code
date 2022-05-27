tmp=input().split()
a=int(tmp[0])
b=float(tmp[1])
b_100 = int(b*100)
ans=(a*b_100)//100
print(ans)


tmp=input().split()
a=int(tmp[0])
b=float(tmp[1])
print((int(a*b)))


b_bef=tmp[1][0:-3]
b_aft=tmp[1][-2:len(tmp[1])]
b_100=int(b_bef+b_aft)
print(b_bef)
print(b_aft)
print(b_100)



tmp=input().split()
a=int(tmp[0])
b_bef=tmp[1][0:-3]
b_aft=tmp[1][-2:len(tmp[1])]
b_100=int(b_bef+b_aft)
ans=(a*b_100)//100
print(ans)