class Solution:
    def reverse(self, x: int) -> int:
        new_num, exp, digits, sig = 0, 0, 0, (-1 if -1*x >= 0 else 1)
        x *= sig
        while x // (10 ** exp):
            digits += 1
            exp += 1
        
        while x:
            new_num += (x % 10) * (10**(digits-1))
            digits -= 1
            x //= 10
        
        new_num *= sig
        return new_num if -(2**31) <= new_num < (2**31) else 0