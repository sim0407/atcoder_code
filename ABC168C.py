import math
a,b,h,m=map(int,input().split())

theta=(11*m-60*h)*math.pi/360
x=math.sqrt(a**2+b**2-2*a*b*math.cos(theta))
print(x)