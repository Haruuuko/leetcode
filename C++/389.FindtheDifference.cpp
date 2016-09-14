/* Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
 */
#include <map>
#include <iostream>
using namespace std;

class Solution {
public:
    char findTheDifference(string s, string t) {
        map<char, int> count;
		for(int i = 0; i < s.size(); i ++){
			if (count.find(s[i])!=count.end()){
				count[s[i]] ++;
			}else{
				count[s[i]] = 1;
			}
		}
		for(int i = 0; i < t.size(); i ++){
			if (count.find(t[i])!=count.end()){
				if (count[t[i]] == 0){
					return t[i];
				}
				count[t[i]] --;
			}else{
				return t[i];
			}
		}
		return 0;
    }
};

int main(){
	Solution test;
	cout << test.findTheDifference("abcd", "abcde") << endl;
	return 0;
}