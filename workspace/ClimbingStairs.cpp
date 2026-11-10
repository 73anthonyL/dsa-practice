// problem: https://neetcode.io/problems/climbing-stairs/question?list=neetcode150
// topic: dynamic programming
// time: O(n)
// space: O(1)
// done
class Solution {
public:
    int climbStairs(int n) {
        int a, b;
        a = b = 1;
        for (int i = 2; i <= n; i++) {
            int curr = a + b;
            swap(b, a);
            swap(b, curr);
        }
        return b;
    }
};