def binary_search(arr,target):
    while lo <= hi:
        mid = (lo + hi) // 2
        # print(lo,hi,mid,val)
        if  arr[mid] >= target:
            hi = mid - 1
        else: 
            lo = mid + 1
    return lo

#returns lowest index for el >= target
