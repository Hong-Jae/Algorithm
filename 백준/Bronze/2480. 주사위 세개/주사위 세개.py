a,b,c=map(int, input().split())
if a==b==c:
  print(10000+a*1000)
elif a==b or b==c or c==a:
  if 2*max((a,b,c)) == sum((a,b,c))-min((a,b,c)):
    print(1000+max((a,b,c))*100)
  elif 2*min((a,b,c)) == sum((a,b,c))-max((a,b,c)):
    print(1000+min((a,b,c))*100)
else:
  print(max((a,b,c))*100)