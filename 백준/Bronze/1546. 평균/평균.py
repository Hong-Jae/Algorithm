TC = int(input())
SC = list(map(int, input().split()))
M = max(SC)
for i in range(TC):
  SC[i] = SC[i]/M*100
print(sum(SC)/TC)