class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        answer, last = [], 0
        for i in range(rowIndex + 1):
            if not i:
                answer.append(1)
                continue
            last = 0
            for j in range(len(answer)):
                z = answer[j]
                answer[j] += last
                last = z
            answer.append(1)

        return answer