/*
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
 */
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
		for(int i = 0; i < numRows; i++){
			vector<int> line;
			line.push_back(1);
			if (i > 0){
				for(int j = 0; j < i-1; j++){
					line.push_back(res[i-1][j] + res[i-1][j+1]);
				}
				line.push_back(1);
			}
			res.push_back(line);
		}
		return res;
    }
};
