A, B, C = map(int, input().split())
D = int(input())

Cs = (C+D)%60
Bm = (B+((C+D)//60))%60
Ah = (A+(B+((C+D)//60))//60)%24


if Ah < 24:
  print(Ah, Bm, Cs)

else:
  print(Ah-24, Bm, Cs)