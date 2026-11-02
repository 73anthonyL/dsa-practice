// problem: https://neetcode.io/problems/duplicate-integer/question?list=neetcode150
// topic: array, hash table, sorting
// time: O(n)
// space: O(n)
// done
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