/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
 */
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> addnums;
		vector<int> res;
		for(int i = 0; i < nums.size(); i++){
			if(addnums.find(nums[i]) == addnums.end()){
				addnums[target - nums[i]] = i;
			}else{
				res.push_back(addnums[nums[i]]);
				res.push_back(i);
				return res;
			}
		}
		return res;
    }
};

int main(){
	Solution test;
	vector<int> s;
	int input;
	while(cin >> input){
		s.push_back(input);
	} 
	vector<int> res = test.twoSum(s,9);
	cout << res[0] << res[1] << endl;
	return 0;
}
