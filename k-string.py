def kstring():
	k=int(input())
	string=input()
	mp={}
	for i in string:
	    mp[i]=mp.get(i,0)+1
	res=[]

	for key,value in mp.items():
	    if value%k==0:
		x=key*(value//k) 
	    else:
		return '-1'
	    res.append(x) 
	return ''.join(res*k) #build the whole segment by multiplying abc*k e.g abcabc
print(kstring())
