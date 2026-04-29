# Deleting First element
arr = [10,70,50,60,80,45,90]
new_arr = []
n = len(arr)

def Delete_First_Element(arr):
  for x in range(1,n):
    new_arr.append(arr[x])
  return new_arr

print(Delete_First_Element(arr))