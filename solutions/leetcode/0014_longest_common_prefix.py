from collections import deque

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        else:
            r, q = 1, deque()

            while r < len(strs):
                if r == 1:
                    for i in range(min(len(strs[0]), len(strs[1]))):
                        if strs[0][i] == strs[1][i]:
                            q.append(strs[0][i])
                        else:
                            break
                else:
                    i, items_to_delete = 0, len(q)
                    for item in q:
                        if i >= len(strs[r]):
                            break
                        if strs[r][i] == item:
                            i += 1
                            items_to_delete -= 1
                        else:
                            break
                    
                    for item in range(items_to_delete):
                        q.pop()
                r += 1

            return("".join(q))



