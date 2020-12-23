class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        lo = 0; hi = len(height) - 1
        # two pointers
        # move the pointer with the smallest side to maximize area
        while lo < hi:
            vol = (hi - lo) * min(height[lo], height[hi])
            res = max(vol, res)
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return res
            