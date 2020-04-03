import random
def pivot(A,prev_left,prev_right):
    if len(A) == 1:
        return A[0]
    x = random.randint(11231,1431424123)
    x = x%(len(A))
    key = A[x]
    left = []
    right = []
    for i in range(len(A)):
        if key <= A[i]:
            left.append(A[i])
        else:
            right.append(A[i])
    if len(left) + prev_left == len(right) + prev_right:
        return key
    elif len(left) + prev_left > len(right) + prev_right:
        return pivot(left,prev_left,prev_right+len(right))
    else:
        return pivot(right,prev_left+len(left),prev_right)

l = list(map(int,input().split()))
print(pivot(l,0,0))
