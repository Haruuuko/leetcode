/*
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
 */
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res;
		int num;
		for(int i = 0; i < rowIndex + 1; i++){
			num = i - 1;
			while(num > 0){
				res[num] += res[num-1];
				num--;
			}
			res.push_back(1);
		}
		return res;
    }
};
