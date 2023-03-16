# k-th largest

import random
nums = [7,3,56,5,8,2]
k = 2
k = len(nums)-k
def quick_select(l,r):
    rand_pivot = random.randint(l,r)
    nums[r], nums[rand_pivot] = nums[rand_pivot], nums[r]
    pivot = nums[r]
    pivot_pos = l
    for i in range(l,r):
        if nums[i]<=pivot:
            nums[pivot_pos], nums[i] = nums[i], nums[pivot_pos]
            pivot_pos+=1
    nums[pivot_pos], nums[r] = nums[r], nums[pivot_pos]

    if pivot_pos>k:
        return quick_select(l,pivot_pos-1)
    if pivot_pos<k:
        return quick_select(pivot_pos+1,r)
    if pivot_pos==k:
        return nums[pivot_pos]
print(quick_select(0, len(nums)-1))