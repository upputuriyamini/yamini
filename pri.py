a=int(input())
k=0
for i in range(2,a):
    if(a%i==0):
    k=k+1
if(k<=0):
        print(is a prime number)
else:
        print(is not a prime number)
