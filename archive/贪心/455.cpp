//
//  455.cpp
//  Leetcode
//
//  Created by 刘冠中 on 2021/1/16.
//
//  有一群孩子和一堆饼干，每个孩子有一个饥饿度，每个饼干都有一个大小。每个孩子只能吃 最多一个饼干，且只有饼干的大小大于孩子的饥饿度时，这个孩子才能吃饱。求解最多有多少孩子可以吃饱。
//  策略：孩子和饼干从小到大排序，贪心

#include <stdio.h>
#include <vector>
using namespace std;

class Solution
{
public:
    int findContentChildren(vector<int> &g, vector<int> &s)
    {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int child = 0, cookie = 0;
        while (child < g.size() && cookie < s.size())
        {
            if (g[child] <= s[cookie])
                ++child;
            ++cookie;
        }
        return child;
    }
};
