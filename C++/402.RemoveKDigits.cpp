/*
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 105 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 */
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string removeKdigits(string num, int k) {
		vector<char> res;
		res.push_back('0');
		for(int i = 0; i < num.length(); i++){
			while(res.back() > num[i] && k > i-res.size()+1){
				res.pop_back();
			}
			res.push_back(num[i]);
		}
		while(res.size() > num.length()-k+1){
			res.pop_back();
		}
		string s = "";
		for(const auto& c : res){
			if(s=="" && c=='0') continue;
			s += c;
		}
		return s=="" ? "0" : s;
    }
};

int main(){
	Solution test;
	cout<<test.removeKdigits("10200",1)<<endl;
	return 0;
}
