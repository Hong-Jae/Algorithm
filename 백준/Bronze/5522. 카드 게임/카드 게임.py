def sums(num, result):
  result.append(num)

result = []
for i in range(5):
  a = int(input())
  sums(a, result)
    
print(sum(result))