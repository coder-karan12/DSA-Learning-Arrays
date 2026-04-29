# Sum of Elements
arr = [2,4,6,8,10]
n = len(arr)

def Sum_Element(arr):
  sum = 0
  for x in range(0,n):
    sum = sum + arr[x]

  return sum

print(Sum_Element(arr))