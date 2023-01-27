n = int(input())
total_x = 0
total_y = 0
total_z = 0
for _ in range(n):
    x,y,z=[int(i) for i in input().split()]
    total_x +=x
    total_y +=y
    total_z +=z
if total_x==total_y==total_z==0:
    print("YES")
else:
    print("NO")
