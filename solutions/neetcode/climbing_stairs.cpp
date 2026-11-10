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