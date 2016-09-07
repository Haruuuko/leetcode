/*
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
 */
#include <iostream>
#include <string>
#include <stack>
#include <ctype.h>
#include <sstream>

using namespace std;

class Solution {
public:
    string decodeString(string s) {
		if(s == "") return "";
        stack<int> num;
		stack<string> str;
		char last;
		for(int i = 0; i < s.size(); i++){
			if(isdigit(s[i])){
				if (isdigit(last)){
					num.top() = num.top() * 10 + (s[i] - '0');
				}else{
					num.push(s[i] - '0');
				}
			}else if(isalpha(s[i])){
				if (isalpha(last) || last == ']'){
					str.top() += s.substr(i,1);
				}else{
					str.push(s.substr(i,1));
				}
			}else if(s[i] == ']'){
				string s2;
				for (int j = 0; j < num.top(); j++){
					s2 += str.top();
				}
				str.pop();
				num.pop();
				if (str.empty()){
					str.push(s2);
				}else{
					str.top() += s2;
				}
				cout << str.top() << endl;
			}
			last = s[i];
		}
		string s3 = str.top();
		str.pop();
		return str.empty()?s3:(str.top()+s3);
    }
};

int main(){
	Solution test;
	string s = "2[2[b]]";
	cout << test.decodeString(s) << endl;
	return 0;
}

