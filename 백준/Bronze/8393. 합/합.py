n = int(input())
a = 0
result = []

def hjm(x,y):
  x.append(y)

for _ in range(n):
  a += 1
  hjm(result, a)

print(sum(result))
