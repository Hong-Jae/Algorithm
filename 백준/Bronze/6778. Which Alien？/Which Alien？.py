result = []

a = int(input())
b = int(input())

if a >= 3 and 4 >= b:
  result.append("TroyMartian")

if 6 >= a and b >= 2:
  result.append("VladSaturnian")

if a <= 2 and 3 >= b:
  result.append("GraemeMercurian")

for results in result:
  print(results)