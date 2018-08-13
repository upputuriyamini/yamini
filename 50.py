def isPowerOfTwo (x):
  return (x and (not(x & (x - 1))) )
N=int(input())
if(isPowerOfTwo(N)):
    print("Yes")
else:
    print("no")
