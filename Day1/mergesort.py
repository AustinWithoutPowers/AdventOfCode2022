# merge sort, it's a goodie
def mergesort(input_array):
  arr1 = input_array[:len(input_array) // 2]
  arr2 = input_array[len(input_array) // 2:]
  # base case
  if len(arr1) + len(arr2) < 3:
    if len(arr1) < 1: return arr2
    if len(arr2) < 1: return arr1
    if arr1[0] < arr2[0]: return arr1 + arr2
    return arr2 + arr1
  
  # othwise, recursion!
  else:
    return_arr = []

    sorted1 = mergesort(arr1)
    sorted2 = mergesort(arr2)

    for _ in range(len(sorted1) + len(sorted2)):
      if len(sorted1) < 1:
        return_arr += sorted2
        break
      elif len(sorted2) < 1:
        return_arr += sorted1
        break
      if sorted1[0] < sorted2[0]: return_arr += [sorted1.pop(0)]
      else: return_arr += [sorted2.pop(0)]
    
    return return_arr