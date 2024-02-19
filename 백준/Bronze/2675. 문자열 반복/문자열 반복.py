TC = int(input())
results = []  

for _ in range(TC):
    R, S = input().split()  
    R = int(R) 
    result = ""

    for i in S:  
        result += i * R  

    results.append(result)

for result in results:
    print(result)