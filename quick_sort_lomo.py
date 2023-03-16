import random

def lomo_partition(arr,low,high):
    rand_idx = random.randint(low,high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
    pivot = arr[high]
    temp_p = low

    for i in range(low, high):
        if arr[i]<=pivot:
            arr[temp_p], arr[i] = arr[i], arr[temp_p]
            temp_p+=1

    arr[temp_p], arr[high] = arr[high], arr[temp_p]
    return temp_p

def quick_sort_lomo(arr,low,high):
    if low < high:
        pivot = lomo_partition(arr,low,high)
        quick_sort_lomo(arr,low, pivot-1)
        quick_sort_lomo(arr, pivot+1, high)
    return arr

print(quick_sort_lomo([7,1,3,2],0,3))