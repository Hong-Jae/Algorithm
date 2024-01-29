class Sort:
    def __init__(self, result):
        self.result = result
        self.result.sort()

    def result_sort(self):
        print(self.result[0], self.result[1], self.result[2])

def main():
    A, B, C = map(int, input().split())
    res = Sort([A, B, C])
    res.result_sort()

if __name__ == "__main__":
    main()