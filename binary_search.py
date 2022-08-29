import numbers

def binary_search(list, target):
  first = 0
  last  = len(list) - 1
  while first < last:
    midpoint = (first+last)//2
    if list[midpoint] < target:
      first = midpoint+1
    elif list[midpoint] > target:
      last = midpoint-1
    else:
      return midpoint
  return None

def verify(index):
  if index is not None:
    print("Target found at index" , index)
  else:
    print("Target Not found in the list")
  
numbers = [1,3,6,8,9,14,20,25,30]

result = binary_search(numbers,10)

verify(result)
