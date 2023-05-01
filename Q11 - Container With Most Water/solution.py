class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # This is a not perfect solution but it works xD

        # This is a two-pointer sliding window problem
        # The idea is to start with the widest window and then move the window
        # inwards to see if we can find a better solution
        # The window is defined by the two pointers i and j
        # The area is defined by the width of the window and the height of the
        # shorter line
        # The area is calculated by min(height[i],height[j]) * (j-i)
        # We start with i = 0 and j = len(height) - 1
        # If height[i] < height[j], we move i to the right
        # If height[i] > height[j], we move j to the left
        # If height[i] == height[j], we move i to the right and j to the left
        # We keep track of the maximum area we have seen so far
        # We stop when i == j
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            max_area = max(max_area,min(height[i],height[j]) * (j-i))
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return max_area