class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idxOfLetter = {}
        l, r, ans, rolling = 0, 0, 0, 0
        while r < len(s):
            if l == r:
                idxOfLetter[s[r]] = r
                rolling += 1
                r += 1
            else:
                if s[r] in idxOfLetter:
                    rolling -= (idxOfLetter[s[r]] - l)
                    while l < idxOfLetter[s[r]]:
                        del idxOfLetter[s[l]]
                        l += 1
                    
                    l = idxOfLetter[s[r]] + 1
                    idxOfLetter[s[r]] = r
                    r += 1
                else:
                    idxOfLetter[s[r]] = r
                    rolling += 1
                    r += 1
            ans = max(ans, rolling)
            
        return ans