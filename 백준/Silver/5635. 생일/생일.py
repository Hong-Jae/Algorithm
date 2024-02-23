TC = int(input())
result = []
result1 = []
result2 = []
name = []
for i in range(TC):
  a,b,c,d = input().split()
  a = str(a)
  b = int(b)
  c = int(c)
  d = int(d)
  y = 2024-d
  result.append(y*365)
  result1.append(y*365+(365-c*365/12))
  result2.append(y*365+(365-c*365/12)-b)
  name.append(a)
  i += 1

if result.count(min(result)) >= 2:
  if result1.count(min(result1)) >= 2:
    print(name[result2.index(min(result2))])
  else:
    print(name[result1.index(min(result1))])
else:
  print(name[result.index(min(result))])

if result.count(max(result)) >= 2:
  if result1.count(max(result1)) >= 2:
    print(name[result2.index(max(result2))])
  else:
    print(name[result1.index(max(result1))])
else:
  print(name[result.index(max(result))]) 