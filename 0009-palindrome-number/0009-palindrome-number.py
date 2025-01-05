class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x 
        reverse = 0
        while (x > 0):
            lastdigit = x % 10
            print("last = ", lastdigit)
            reverse = reverse * 10 + lastdigit
            print("rev = ", reverse)
            x = x // 10
        
        return True if reverse == num else False