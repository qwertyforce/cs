def binary_search(arr,target):
    l,r = 0, len(arr)     
    while l+1<r:   # [l, r)  =>  [l, r-1] a[r] > x
        mid =  l+ (r-l)//2
        if arr[mid] > target:
            r = mid
        else:
            l = mid
    return l if arr[l]==target else -1
