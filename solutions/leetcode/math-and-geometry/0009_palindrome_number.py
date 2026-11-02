class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        digit = 1
        palindrome = True
        while (x > (10**digit)-1):
            digit += 1
        
        for i in range(digit // 2):
            if ((x % (10**(i+1))) // (10**i)) != ((x % (10**(digit-i))) // (10**(digit-i-1))):
                palindrome = False
                break
        return palindrome