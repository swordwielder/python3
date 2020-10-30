

s = int(input())
n = int(input())
a={}
for i in range(n):
    car_id, tip = [int(j) for j in input().split()]
    if car_id not in a:
        a[car_id]=tip

car_ids = input().split()
t=0
for i in car_ids:
    if int(i)<0 and abs(int(i)) in a:
        t+=a[abs(int(i))]


print(t)
