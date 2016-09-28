/*
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
 */
class Solution {
public:
    int getSum(int a, int b) {
        while(b){
            int sum = a ^ b;
            int tmp = (a & b) << 1;
            a = sum;
            b = tmp;
        }
        return a;
    }
};
