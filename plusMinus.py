#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

def plusMinus(arr,n):
  positive=0
  negative=0
  zero=0
  for i in range(n):
    if arr[i] > 0:
      positive = positive+1
    elif arr[i] < 0:
      negative =negative+1
    else:
      zero=zero+1

  res_positive=positive/n
  res_negative=negative/n
  res_zero=zero/n

  print(round(res_positive,4))
  print(round(res_negative,4))
  print(round(res_zero,4))


arr=[-4,3,-9,0,4,1] 
plusMinus(arr,6)  
