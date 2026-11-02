class Solution {
public:
    int rob(vector<int>& nums) {
        vector<vector<int>> dp(nums.size(), vector<int>(2));
        // need to keep track of the optimal solution for when
        // the last one was used and the last one wasnt used


        for (int i = 0; i < nums.size(); i++) {
            // DP vector maintains the best way to rob houses 0-i
            // 0 for current unrobbed, 1 for current robbed
            if (!i) {
                dp[i][1] = nums[i];
                continue;
            }

            dp[i][0] = max(dp[i-1][0], dp[i-1][1]);
            dp[i][1] = dp[i-1][0] + nums[i];

        }

        return max(dp[nums.size() - 1][0], dp[nums.size() - 1][1]);
    }
};
