# Minimum Element
arr = [1,3,4,-7,-4,5,6,-6,8,9,7]
n = len(arr)

def Min_Element(arr):
  min = arr[0]
  for x in range(1,n):
    if arr[x] < min:
      min = arr[x]
  return min

print(Min_Element(arr))