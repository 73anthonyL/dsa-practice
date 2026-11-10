// problem: https://neetcode.io/problems/min-cost-climbing-stairs/
// topic: dynamic programming
// time: O(n)
// space: O(1)
// done
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        switch (cost.size()) {
            case 0:
                return 0;
            case 1:
                return cost[0];
            case 2:
                return min(cost[0], cost[1]);
            default:
                int a, b;
                a = b = 0;
                for (int i = 2; i <= cost.size(); i++) {
                    int curr = min(b + cost[i-1], a + cost[i-2]);
                    swap(a, b);
                    swap(b, curr);
                }
                return b;
        }
    }
};
