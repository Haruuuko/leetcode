/*
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 */
#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestSubstring(string s, int k) {
		if (s.size() < k) return 0;
		map<char, int> count;
		vector<char> split;
		int sub = 0, res = 0;
        for(int i = 0; i < s.size(); i++){
			count[s[i]] ++;
		}
		for(map<char, int>::iterator i=count.begin(); i!=count.end(); i++){
			if(i->second < k) split.push_back(i->first);
		}
		if (split.size() == 0) return s.size();

		for(int i = 0; i < s.size(); i++){
			vector<char>::iterator iter=find(split.begin(), split.end(), s[i]);
			if(iter != split.end() || i == s.size()-1){
				int len = (iter == split.end() && i==(s.size()-1)) ? i-sub+1 : i-sub;
				int r = longestSubstring(s.substr(sub,len), k);
				sub = i+1;
				res = max(res, r);
			}
		}
		return res;
    }
};

int main(){
	Solution test;
	string s = "ababbc";
	cout << test.longestSubstring(s,2) << endl;
	return 0;
}

