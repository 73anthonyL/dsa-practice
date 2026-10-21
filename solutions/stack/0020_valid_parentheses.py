class Solution:
    def isValid(self, s: str) -> bool:
        rou, cur, squ = deque(), deque(), deque()
        for i in range(len(s)):
            if s[i] == '(':
                rou.append(i)
            elif s[i] == '{':
                cur.append(i)
            elif s[i] == '[':
                squ.append(i)
            elif s[i] == ')':
                if not len(rou) or (False if not len(cur) else cur[-1] > rou[-1]) or (False if not len(squ) else squ[-1] > rou[-1]):
                    return False
                rou.pop()
            elif s[i] == '}':
                if not len(cur) or (False if not len(rou) else rou[-1] > cur[-1]) or (False if not len(squ) else squ[-1] > cur[-1]):
                    return False
                cur.pop()  
            elif s[i] == ']':
                if not len(squ) or (False if not len(cur) else cur[-1] > squ[-1]) or (False if not len(rou) else rou[-1] > squ[-1]):
                    return False
                squ.pop() 
        return not (len(rou) or len(cur) or len(squ))
