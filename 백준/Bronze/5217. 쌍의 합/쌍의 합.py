T = int(input())  # 테스트 케이스의 수
result = []

for _ in range(T):
    n = int(input())
    pairs = []
    for i in range(1, n//2 + 1):  # n//2까지 반복
        if i != n - i:  # 두 수가 다를 경우만 처리
            pairs.append(f"{i} {n-i}")
    # 쌍을 문자열로 만들어 result에 추가
    result.append(f"Pairs for {n}: " + ", ".join(pairs))

# 모든 결과를 한 번에 출력
for line in result:
    print(line)