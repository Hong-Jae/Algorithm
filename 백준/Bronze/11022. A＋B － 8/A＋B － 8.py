T = int(input())
case = 1

while case <= T:
    A, B = map(int, input().split())
    result = A+B
    print(f"Case #{case}: {A} + {B} = {result}")
    case += 1