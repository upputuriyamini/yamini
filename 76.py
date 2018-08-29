n=int(raw_input())
f=0
for i in range (1,n):
             if n%i==0:
                   f=i
if f>1:
      print 'yes'
else:
      print 'no'
