/*
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
 */

class Solution {
public:
    vector<string> readBinaryWatch(int num) {
        vector<vector<int>> hour, minute;
        vector<string> res;
        for(int i = 0; i < num+1; i++){
            hour.push_back(validNum(4,i));
            minute.push_back(validNum(6,num-i));
        }
        for(int i = 0; i < num+1; i++){
            for(const auto& h : hour[i]){
                for(const auto& m : minute[i]){
                    string t = m<10?to_string(h).append(":0").append(to_string(m)):to_string(h).append(":").append(to_string(m));
                    res.push_back(t);
                }
            }
        }
        return res;
    }
    
    vector<int> validNum(int n, int valid){
        int max = n==4 ? 12 : 60 ;
        vector<int> res;
        for(int i = 0; i < max; i++){
            int count = 0, num = i;
            while(num){
                count += num & 1;
                num >>= 1;
            }
            if(count==valid) res.push_back(i);
        }
        return res;
    }
};
