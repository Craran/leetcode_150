from typing import List
# class Solution:
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    result = []
    i = j = 0
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    if i < m:
        for k in range(i, m):
            result.append(nums1[k])
    else:
        for k in range(j, n):
            result.append(nums2[k])

    for _ in range(m + n):
        nums1[_] = result[_]
        return 


# Solution.merge(Solution, [0], 0, [1], 1)
nums1 = [0]
nums2 = [1]
merge(nums1, 0, nums2, 1)
print(nums1)