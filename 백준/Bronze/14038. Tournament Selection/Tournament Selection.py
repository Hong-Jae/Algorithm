result = []
total = []
for _ in range(6):
  A = str(input())
  result.append(A)

for i in range(0,6):
  if result[i] == "W":
    total.append("W")
  i += 1

k = total.count("W")
if k >= 5:
  print(1)
elif k >= 3:
  print(2)
elif k >= 1:
  print(3)
else:
  print(-1)