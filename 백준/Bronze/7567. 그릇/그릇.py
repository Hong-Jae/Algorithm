a = str(input())
sum = 0
for i in range(len(a)):
    if i+1 <= len(a) and i-1 >=0:
        if a[i] != a[i:i+1] or (a[i-1] != a[i] and a[i] == a[i:i+1]):
            sum += 10
        else:
            sum += 5
    elif i == 0:
        if a[i] != a[i:i+1]:
            sum += 10
        else:
            sum += 5
    else:
        break    
print(sum+5)