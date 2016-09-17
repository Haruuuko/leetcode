/*
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
 */
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length()) return false;
        unordered_map<char, int> count;
        for(const auto& c : s){
            ++count[c];
        }
        for(const auto& c : t){
            if(count.count(c) && count[c]){
                count[c]--;
            }else{
                return false;
            }
        }
        return true;
    }
};
