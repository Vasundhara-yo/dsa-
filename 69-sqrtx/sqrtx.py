class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x  # 0 and 1 are easy cases
        
        left, right = 1, x // 2  # The sqrt of x is never more than x/2 for x > 1
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right  # right is the floor of sqrt(x)



        