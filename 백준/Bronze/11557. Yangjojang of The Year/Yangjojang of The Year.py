TC = int(input())
for _ in range(TC):
  Test = int(input())
  result_name = []
  result_num = []
  for _ in range(Test):
    a, b = input().split()
    b = int(b)
    result_name.append(a)
    result_num.append(b)
  maxx = max(result_num)
  num = result_num.index(maxx)
  name = result_name[int(num)]
  print(name)