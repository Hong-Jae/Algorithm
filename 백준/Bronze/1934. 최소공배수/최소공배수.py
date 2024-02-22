import math
TC = int(input())
for _ in range(TC):
  a,b = map(int, input().split())
  print(math.lcm(a,b))