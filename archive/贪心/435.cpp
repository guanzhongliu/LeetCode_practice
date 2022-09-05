//
//  435.cpp
//  Leetcode
//
//  Created by 刘冠中 on 2021/1/16.
//
//  给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
//  策略：按照右边界从小到大排序，依次选择删除目标，右边界越小，留给其他区间的空间越多(这题好坑，题干里没说有边界为负数和区间数量为0的情况）

#include <vector>
#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    static bool comp(vector<int>& a, vector<int>& b){
        return a[1] < b[1];
    }
    
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) {
            return 0;
        }
        int num = intervals.size();
        sort(intervals.begin(), intervals.end(), comp);
        int res = 0, last = intervals[0][0];
        for(int i = 0; i < num; i++){
            if(intervals[i][0] < last){
                res++;
            }
            else{
                last = intervals[i][1];
            }
            
        }
        
        return res;
    }
};
