import math

prime = [True for _ in range(1001)] # True - 소수 / False - 소수가 아님
prime[1] = 0
prime[2] = 1
prime[3] = 1

for i in range(1001):
  for x in range(2, int(math.sqrt(i))+1):
    if i % x == 0:
      prime[i] = False
      break

for i in range(len(prime)):
  if prime[i]:
    print(i, end = " ")
    