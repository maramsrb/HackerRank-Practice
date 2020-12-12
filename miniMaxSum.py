#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

def miniMaxSum(arr):
  arr.sort()
  sum1=0
  sum2=0

  print(arr)
  for i in range(4):
    sum1= sum1+arr[i]

  for i in range(4,0,-1): 
    sum2=sum2+arr[i]
  
  return sum1,sum2  


arr=[1,3,5,7,9]
print(miniMaxSum(arr))