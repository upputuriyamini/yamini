N,M=map(int,raw_input().split())
A=[int(x) for x in raw_input().split()]
B=[int(y) for y in raw_input().split()]
if set(B).issubset(A):
                  print('YES')
else:
                  print('NO')
