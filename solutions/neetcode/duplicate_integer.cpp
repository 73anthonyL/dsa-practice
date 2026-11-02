class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, bool> m;
        for (int c: nums) {
            if (m[c]) {
                return true;
            }
            m[c] = true;
        }
        return false;
    }
};