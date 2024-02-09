A = int(input())
result = []

def countlen(a):
  t = 0
  for i in a:
    if i != ' ': # 만약 줄바꿈도 포함시키려면, and i != '\n'추가할 것
      t += 1
  return t

for _ in range(A):
  a = str(input())
  num = a.count('A') + a.count('E') + a.count('I') + a.count('O') + a.count('U') + a.count('a') + a.count('e') + a.count('i') + a.count('o') + a.count('u')
  nnum = countlen(a)
  numr = nnum - num
  result.append(f"{numr} {num}")

for line in result:
  print("".join(line))