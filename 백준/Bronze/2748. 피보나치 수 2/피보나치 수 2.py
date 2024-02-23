def Hi(a):
  S1 = 0
  S2 = 1
  for i in range(a+2):
    if i >=2:
      if i%2 ==0:
        S1 = S1+S2
      else:
        S2 = S1+S2
  if a>=2 and a%2==0:
    print(S1)
  elif a==1:
    print(1)
  else:
    print(S2)

Hi(int(input()))