global answer

def JG(sum, n): 
  global answer
  if sum == n:
    answer += 1
    return
  if sum > n:
    return
  for i in range(1,4):
    JG(sum+i, n)

n= int(input())
sum = 0
hjm = []

for _ in range(n):
  answer = 0
  a = int(input())
  JG(sum, a)
  hjm.append(answer)

for k in hjm:
  print(k)