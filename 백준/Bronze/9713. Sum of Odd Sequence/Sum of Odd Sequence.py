TC = int(input())
for _ in range(TC):
    N = int(input())
    # 1부터 N까지 홀수의 합을 계산
    sum_of_odds = ((N + 1) // 2) ** 2
    print(sum_of_odds)
