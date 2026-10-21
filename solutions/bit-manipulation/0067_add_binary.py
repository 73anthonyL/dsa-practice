class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a
    
        a = ("0"*(len(b)-len(a))) + a
        
        sum = ""
        i = len(b) - 1
        carry = False
        while i >= 0:
            if a[i] != b[i]:
                if carry:
                    sum += '0'
                else:
                    sum += '1'
            elif a[i] == '1':
                if carry:
                    sum += '1'
                else:
                    sum += '0'
                    carry = True
            else:
                if carry:
                    sum += '1'
                    carry = False
                else:
                    sum += '0'
            i -= 1

        if carry:
            sum += '1'
        return sum[::-1]
        

