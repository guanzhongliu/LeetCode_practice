//
//  135.cpp
//  Leetcode
//
//  Created by 刘冠中 on 2021/1/16.
//
//  一群孩子站成一排，每一个孩子有自己的评分。现在需要给这些孩子发糖果，规则是如果一 个孩子的评分比自己身旁的一个孩子要高，那么这个孩子就必须得到比身旁孩子更多的糖果;所有孩子至少要有一个糖果。求解最少需要多少个糖果。
//  策略：前后扫两遍数组，每一遍都满足分数高的糖果更多

#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        int num = ratings.size();
        vector<int> candies(num, 1);
        
        for(int i = 1; i < num; i++){
            if(ratings[i] > ratings[i - 1])
                candies[i] = candies[i - 1] + 1;
        }
        
        int ans = candies[num - 1];
        
        for(int i = num - 1; i > 0; i--){
            if(ratings[i] < ratings[i - 1])
                candies[i - 1] = max(candies[i] + 1, candies[i - 1]);
            ans += candies[i - 1];
        }
        
        return ans;
    }
};
