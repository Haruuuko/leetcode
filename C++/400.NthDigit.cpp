/*
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
 */
#include <iostream>
#include <math.h>
using namespace std;
class Solution {
public:
    int findNthDigit(int n) {
        if(n<10) return n;
        long long s=9, i=1, tmp=0, sum=9;
        while(sum<n){
            tmp += s;
            s *= 10;
            sum += s*(++i);
        }
        sum -= s*i;
        s/=10;
        int num = tmp + (n-sum)/i;
        int res = (n-sum)%i?(num+1)/pow(10,i-(n-sum)%i):num;
        return res%10;
    }
};

int main(){
	Solution test;
	cout<<test.findNthDigit(1000000000)<<endl;
	return 0;
}
