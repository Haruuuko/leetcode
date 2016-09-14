/*
Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
*/

#include <iostream>
#include <vector>
#include <array>
using namespace std;

class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        int n = 1;
		int sum = 0;
		int first = 0;
        int len = A.size();
        if (len == 0) return 0;
        int fv[len] = {0};
        for(int i = 0; i < len; i++){
            sum += A[i];
            first += i * A[i];
        }
        int max = first;
		fv[0] = first;
        while(n < len){
            fv[n] = fv[n-1] + sum - len * A[len-n];
			cout<<fv[n]<<endl;
			if(fv[n] > max) max = fv[n];
            n++;
        }
        return max;
	}
};

int main(){
	Solution test;
	vector<int> A;
	A.push_back(1);
	A.push_back(2);
	A.push_back(3);
	A.push_back(4);
	A.push_back(5);
	A.push_back(6);
	A.push_back(7);
	A.push_back(8);
	A.push_back(9);
	A.push_back(10);
	cout << test.maxRotateFunction(A) << endl;
	return 0;
}
