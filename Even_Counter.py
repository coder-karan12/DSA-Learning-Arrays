# Even/Odd Counter
arr = [2, 5, 8, 7, 10]

def Number_Counter(arr):
  even = 0
  odd = 0

  for x in range(len(arr)):

    if arr[x] % 2 == 0:
      even += 1
    else:
      odd += 1

  return even, odd

print(Number_Counter(arr))