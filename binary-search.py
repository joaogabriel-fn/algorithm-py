def binary_search(arr, t):
  low = 0
  high = len(arr)
  steps = 0

  while low < high:
    steps += 1
    mid = int((low+high)/2)

    if arr[mid] == t:
       print("steps: ", steps)
       return mid
    elif arr[mid] < t:
       low = mid+1
    else:
       high = mid

  return -1

    
       

def array_generator(start, end, step):
    arr = [i for i in range(start, end, step)]
    return arr

arr = array_generator(1, 81, 1)

print(arr)
binary_search(arr, 3)
