def delete_duplicates(nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    for i in range(j, len(nums)):
        nums[i] = 0
    return nums


if __name__ == "__main__":
    print(delete_duplicates([0, 1, 2, 3, 3, 3, 5, 5, 7]))
    print(delete_duplicates([0, 0, 1, 1, 1, 2, 3, 4, 4, 5, 5]))