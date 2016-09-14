/*
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
 */
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <array> 
using namespace std;
class Solution {
public:
    Solution(vector<int> nums) {
       _nums = nums;
	   srand(0);
    }
    
    int pick(int target) {
        int count=0, ret=-1;
        for(int i=0;i<_nums.size();++i) {
            if(_nums[i]==target) {
                ++count;
                if(rand()%count==0)
                    ret=i;
            }
        }
        return ret;
    }
private:
    vector<int> _nums;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
int main(){
	vector<int> nums;
	nums.push_back(1);
	nums.push_back(2);
	nums.push_back(3);
	nums.push_back(3);
	nums.push_back(3);
	nums.push_back(3);
	Solution obj(nums);
	int param_1 = obj.pick(3);
	cout<<param_1<<endl;
	return 0;
}
