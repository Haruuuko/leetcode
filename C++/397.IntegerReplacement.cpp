/*
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
 */

#include <iostream>
using namespace std;
class Solution {
public:
    int integerReplacement(int n) {
		if(n==1) return 0;
		if(n==INT_MAX) return 32;
		if (n%2==0) return integerReplacement(n/2) + 1;
        return min(integerReplacement(n-1), integerReplacement(n+1)) + 1;
    }
};

int main(){
	Solution test;
	cout<<test.integerReplacement(2147483647)<<endl;
	return 0;
}
