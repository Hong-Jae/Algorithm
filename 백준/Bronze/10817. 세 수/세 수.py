a, b, c = map(int, input().split())
if (a>=b and b>=c)or(c>=b and b>=a):
  print(b)
elif (b>=a and a>=c)or(c>=a and a>=b):
  print(a)
elif (a>=c and c>=b)or(b>=c and c>=a):
  print(c)