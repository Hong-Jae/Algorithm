class MarsMath:
    def __init__(self, expressions):
        self.expressions = expressions

    def calculate(self, expression):
        result = float(expression[0])
        for operator in expression[1:]:
            if operator == '@':
                result *= 3
            elif operator == '%':
                result += 5
            elif operator == '#':
                result -= 7
        return f"{result:.2f}"

    def solve_all(self):
        return [self.calculate(k) for k in self.expressions]

def main():
    T = int(input())
    expressions = [input().split() for _ in range(T)]
    
    mars_math = MarsMath(expressions)
    kk = mars_math.solve_all()

    for result in kk:
        print(result)

if __name__ == "__main__":
    main()