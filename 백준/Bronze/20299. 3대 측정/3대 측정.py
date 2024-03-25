
N, a, b = map(int, input().split())
HJ = []
total = 0
for _ in range(N):
  x = list(map(int, input().split()))
  if sum(x) >= a and min(x) >= b:
    HJ.extend(x)
    total += 1
  
print(total) 
for k in HJ:
  print(k, end=" ")