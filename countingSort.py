from typing import List

def countingSort(nums: List[int]) -> List[int]:
    min = nums[0]
    max = nums[0]
    for i in range(1, len(nums)):
        if min > nums[i]:
            min = nums[i]
        if max < nums[i]:
            max = nums[i]

    counts = [0] * (max - min + 1)

    for i in range(len(nums)):
        counts[nums[i] - min] += 1
    # print("Init counts: ", counts)

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    # print("Modified counts: ", counts)

    sorted = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        sorted[counts[nums[i] - min] - 1] = nums[i]
        counts[nums[i] - min] -= 1
    # print(sorted)

    return sorted

if __name__ == '__main__':
    nums = [2, 5, 3, 0, 2, 3, 0, 3]
    print(nums)
    print(countingSort(nums))

    nums = [2, 5, 3, 2, 3, 3]
    print(nums)
    print(countingSort(nums))

    nums = [2, -1, 0, 1, -2]
    print(nums)
    print(countingSort(nums))

    nums = [2, -1, 1, 0, -1, 2, -2]
    print(nums)
    print(countingSort(nums))

