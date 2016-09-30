/*
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
 */
class Solution {
public:
    int firstUniqChar(string s) {
        int n = s.length();
        unordered_map<char, int> count;
        for(int i = 0; i < n; i++){
            count[s[i]] ++;
        }
        for(int i = 0; i < n; i++){
            if(count[s[i]]==1) return i;
        }
        return -1;
    }
};
