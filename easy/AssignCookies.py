class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # you want to assign each child the smallest cookie that will satisfy them
        # iterate through all the cookies in decreasing size
        # for each cookie continue the pointer in the children (decreasing greed order) and assign
        # to the greediest child

        g.sort()
        s.sort()

        content_children = 0
        j = len(g) - 1
        for i in reversed(range(len(s))):
            while j >= 0:
                if s[i] >= g[j]:
                    content_children += 1
                    j -= 1
                    break
                j -= 1
        
        return content_children

        