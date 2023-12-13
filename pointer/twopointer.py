# Q: ypu have sorted array 
# find the numbers whose pair of sum = 0

arr = [-9, -4, -1, 1, 4, 8, 11]

left = 0
right = len(arr) - 1

while left < right:
    sum = arr[left] + arr[right]
    if sum == 0:
        print(arr[left])
        print(arr[right])
        break
    elif sum < 0:
        left += 1
    else:
        right -= 1