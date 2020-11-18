def dutch_flag_partition_sol_1(pivot_idx, arr):
    pivot = arr[pivot_idx]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                break
        
    for i in reversed(range(len(arr))):
        if arr[i] < pivot:
            break

        for j in reversed(range(i)):
            if arr[j] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                break
    return arr

# more optimize
def dutch_flag_partition_sol(pivot_idx, arr):
    pivot = arr[pivot_idx]
    smaller_idx, equal_idx = 0, 0
    larger_idx = len(arr) - 1
    while equal_idx <= larger_idx:
        if arr[equal_idx] < pivot:
            arr[smaller_idx], arr[equal_idx] = arr[equal_idx], arr[smaller_idx]
            smaller_idx += 1
            equal_idx += 1
        elif arr[equal_idx] == pivot:
            equal_idx += 1
        else: # arr[equal_idx] > pivot
            arr[equal_idx], arr[larger_idx] = arr[larger_idx], arr[equal_idx]
            larger_idx -= 1
    return arr

if __name__ == "__main__":
    idx = 3
    arr = [8, 2, 14, 4, 3, 5, 2, 4 ,5, 6, 7, 3, 4, 5]
    print(dutch_flag_partition_sol(idx, arr))