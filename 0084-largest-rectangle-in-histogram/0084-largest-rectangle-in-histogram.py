class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []   #[index, height]
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            # if top values height > curr
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # i - index is the width since i is our current and index is from the popped where it was smaller
                max_area = max(max_area, height * (i - index))
                # extend the index backwards
                start = index
            
            # we want to reset to the start
            stack.append((start,h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area
