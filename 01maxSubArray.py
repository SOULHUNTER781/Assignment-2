def maxCrossSubarray(A,low,mid,high):
    left_sum = -1000000000000
    max_left = mid
    sum = 0
    for i in range(mid,low-1,-1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -1000000000000
    max_right = mid
    sum = 0
    for i in range(mid+1,high+1):
        sum = sum + A[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return max_left, max_right, (left_sum + right_sum)
    


def maxSubArray(A,low,high):
    if low == high:
        return low, high, A[low]
    else:
        mid = low + high
        mid //= 2
        li, lj, left_sum = maxSubArray(A,low,mid)
        ri, rj, right_sum = maxSubArray(A,mid+1,high)
        ci, cj, cross_sum = maxCrossSubarray(A,low,mid,high)
        if left_sum > right_sum and left_sum > cross_sum:
            return li, lj, left_sum
        elif right_sum > left_sum and right_sum > cross_sum:
            return ri, rj, right_sum
        else:
            return ci, cj, cross_sum
        


l = list(map(float,input().split()))
n = len(l)
left, right, maxl = maxSubArray(l,0,n-1)
print(left,right)
for i in range(left,right+1):
    print(l[i], end = " ")
print()
