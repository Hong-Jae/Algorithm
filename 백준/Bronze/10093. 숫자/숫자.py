a, b = map(int, input().split())

def SHR(a,b):
  global HJM
  if a != b:
    HJM = abs(b - a) - 1
  else:
    HJM = 0
  print(int(HJM))

def SHR2(a,b):
  global result
  result = []
  for i in range(HJM):
    if a > b:
      result.append(f"{b+i+1}")    
    elif b > a:
      result.append(f"{a+i+1}")    
    else:
      break
  print(" ".join(result))

SHR(a,b)
SHR2(a,b)