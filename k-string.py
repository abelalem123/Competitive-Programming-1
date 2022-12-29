
k=int(input())
string=input()
mp={}
for i in string:
    mp[i]=mp.get(i,0)+1
res=[]
flag=True
#a:2,b:2,c:2
#we want 2-string
for key,value in mp.items():
    if value%k==0:
        x=[key]*(value//k) #build the k string i.e a*2//2 a*1
    else:
        flag=False
        break
    res.extend(x) #build the first segment of the k-string e.g abc
new=[]
if not flag:
    print("-1")
else:
    new.extend(res*k) #build the whole segment by multiplying abc*k e.g abcabc
    print(''.join(new))
