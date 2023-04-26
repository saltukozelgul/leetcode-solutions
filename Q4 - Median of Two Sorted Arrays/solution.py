class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = self.merge(nums1, nums2)
        if len(merged) % 2 == 0:
            return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2.0
        else:
            return merged[len(merged) // 2]

    def merge(self, nums1, nums2):
        merged_array = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged_array.append(nums1[i])
                i += 1
            else:
                merged_array.append(nums2[j])
                j += 1
        if i < len(nums1):
            merged_array.extend(nums1[i:])
        if j < len(nums2):
            merged_array.extend(nums2[j:])
        return merged_array