# Maximum element
arr = [1,3,4,5,6,8,9,7]
n = len(arr)

def Max_Element(arr):
  max = arr[0]
  for x in range(1,n):
    if arr[x] > max:
      max = arr[x]
  return max

print(Max_Element(arr))