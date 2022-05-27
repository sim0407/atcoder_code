n=int(input())
pattern=0
letter=0
for i in range(100):
    pattern += (26 ** i)
    if pattern >= n:
        letter = i
        break

name_rev=''
count = n
for i in range(letter):
    name_rev += 


name=[]
for i in range(1000000000000001):
    


#here
n=int(input())
def num2alpha(num):
    if num<=26:
        return chr(64+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num%26)
ans=num2alpha(n).lower()
print(ans)