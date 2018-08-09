lower,upper=map(int,raw_input().split())
for num in range(lower,upper):
    temp=num
    sum=0
    while(temp>0):
          digit=temp%10
          sum=sum+digit**3
          temp=temp/10
          if(sum==num):
              print(num)
               
