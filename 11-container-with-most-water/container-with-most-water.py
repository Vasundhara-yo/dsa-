class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        l = 0
        r = n - 1

        while l < r:
            width = r - l
            area = min(height[l], height[r]) * width

            if area > max_area:
                max_area = area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
    
        

       
    