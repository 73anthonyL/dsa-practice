class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        answer = []
        for i in range(numRows):
            if not i:
                answer.append([1])
                continue

            curr = []
            for j in range(i + 1):
                if (not j) or (j == i):
                    curr.append(1)
                else:
                    curr.append(answer[i - 1][j-1] + answer[i - 1][j])
            answer.append(curr)

        return answer
        