a,b = map(int, input().split())
if b-45<0:
  a -= 1
  b = b-45+60
  if a<0:
    a += 24
else:
  b -= 45
print(a,b)