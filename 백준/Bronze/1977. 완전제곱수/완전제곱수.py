a = int(input())
b = int(input())
n = 0
while b >= a:
  for i in range(a,b+1):
    if i**(1/2) == int(i**(1/2)):
      n += i  
    if n == 0 and i == b:
      n = -1     
  print(n)
  break
  

while b >= a:
  for i in range(a,b+1):
    if i**(1/2) == int(i**(1/2)):
      print(i)
      quit()
  break