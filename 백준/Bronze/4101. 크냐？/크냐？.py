class exercise:
  def __init__(self, result):
    self.result = result
    self.sort = sorted(self.result)
  
  def compare(self):
    if self.result[0] == self.sort[0]:
      return 'No'
    else:
      return 'Yes'

def main():
  output = []
  while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
      break
    result = exercise([A,B])
    output.append(result.compare())
  
  print("\n".join(output))

if __name__ == "__main__":
  main()