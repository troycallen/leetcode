class Solution:
    def myAtoi(self, s: str) -> int:
        # Constants for 32-bit signed int range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i, n = 0, len(s)
        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Handle empty/whitespace only
        if i == n:
            return 0

        # Handle sign
        sign = 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        num = 0
        # Convert digits
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow/underflow before adding digit
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1
        
        return sign * num
