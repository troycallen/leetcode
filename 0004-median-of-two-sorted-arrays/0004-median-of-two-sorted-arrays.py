class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        merged = nums1 + nums2
        merged.sort()

        merged_len = len(merged)

        if merged_len % 2 != 0:
            return merged[merged_len // 2]
        else:
            return (merged[merged_len // 2 - 1] + merged[merged_len // 2]) / 2