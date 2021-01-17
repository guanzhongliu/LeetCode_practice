//
//  1232.cpp
//  Leetcode
//
//  Created by 刘冠中 on 2021/1/17.
//
//  在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false
//  策略：那就遍历一遍吧

#include <stdio.h>
#include <vector>
using namespace std;

class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& c) {
        int len = c.size();
        for(int i = 2; i < len; i++)
            if((c[1][1]-c[0][1])*(c[i][0]-c[0][0])!=(c[i][1]-c[0][1])*(c[1][0]-c[0][0]))
                        return false;
        return true;
    }
};
