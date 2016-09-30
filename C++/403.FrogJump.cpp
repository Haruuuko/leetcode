/*
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog has just jumped k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:
[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
 */
#include <iostream>
#include <vector>
#include <queue>
#include <array>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool canCross(vector<int>& stones) {
		unordered_map<int,int> stone;
        queue<array<int,2> > q;
		unordered_map<int,vector<int> > v;
		q.push({0,0});
		v[0].push_back(0);
		for (int i = 0; i < stones.size(); i++) {
			stone[stones[i]] = i;
        }
		while(!q.empty()){
			array<int,2> tmp = q.front();
			q.pop();
			if(tmp[0]==stones.back()) return true;
			for(int i = tmp[1]-1; i<tmp[1]+2; i++){
				int vf=0;
				for(const auto& arr : v[tmp[0]+i]){
					if(arr==i) vf=1;
				}
				if (i>0 && !vf && stone.count(tmp[0]+i)){
					v[tmp[0]+i].push_back(i);
					q.push({tmp[0]+i,i});
				}
			}
		}
		return false;
    }
};

int main(){
	Solution test;
	vector<int> s;
	s.push_back(0);
	s.push_back(1);
	s.push_back(3);
	s.push_back(5);
	s.push_back(6);
	s.push_back(8);
	s.push_back(12);
	s.push_back(17);
	cout<<test.canCross(s)<<endl;
	return 0;
}