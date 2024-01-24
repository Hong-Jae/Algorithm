A, B = map(int, input().split())
C = int(input())

if (B+C)//60 < 1:
  if A < 24:
    result = B+C
    print(str(A)+" "+str(result))
  else:
    result_24 = B+C
    print(str(A-24)+" "+str(result_24))
 
else:
  if A+((B+C)//60) < 24:
    result1 = A+((B+C)//60)
    result2 = (B+C)%60
    print(str(result1)+" "+str(result2))

  else:
    result1_24 = A+((B+C)//60)
    result2_24 = (B+C)%60
    print(str(result1_24-24)+" "+str(result2_24))