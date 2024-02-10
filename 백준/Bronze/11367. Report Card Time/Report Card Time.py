TestCase = int(input())
result = []
for _ in range(TestCase):
  Name, Num = input().split()
  Num = int(Num)
  if Num >= 97:
    result.append(f"{Name} A+")
  elif Num >= 90:
    result.append(f"{Name} A")
  elif Num >= 87:
    result.append(f"{Name} B+")
  elif Num >= 80:
    result.append(f"{Name} B")
  elif Num >= 77:
    result.append(f"{Name} C+")
  elif Num >= 70:
    result.append(f"{Name} C")
  elif Num >= 67:
    result.append(f"{Name} D+")
  elif Num >= 60:
    result.append(f"{Name} D")
  else:
    result.append(f"{Name} F")
for line in result:
  print("".join(line))