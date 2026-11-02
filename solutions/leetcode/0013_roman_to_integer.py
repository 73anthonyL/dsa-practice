class Solution:
    def romanToInt(self, s: str) -> int:
        prev, sum = "", 0
        hirearchy = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        for c in s:
            if prev:
                if (prev + c) in hirearchy:
                    sum += hirearchy[prev + c]
                    prev = ""
                else:
                    sum += hirearchy[prev]
                    prev = c
            else:
                prev = c
        
        if prev:
            sum += hirearchy[prev]
            
        return sum
        