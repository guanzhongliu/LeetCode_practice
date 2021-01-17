//
//  122.cpp
//  Leetcode
//
//  Created by 刘冠中 on 2021/1/17.
//
//  给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
//  策略：贪心，只要第二天降价就先卖出再买入; 官方题解实现方式更好，更简洁

#include <vector>
#include <stdio.h>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int len = prices.size();
        int ans = 0, price = prices[0];
        for(int i = 0; i < len-1; i++){
            if(prices[i + 1] < prices[i]){
                ans += prices[i] - price;
                price = prices[i + 1];
            }
        }
        ans += prices[len - 1] - price;
    return ans;
    }
};

class Solution_official {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        int n = prices.size();
        for (int i = 1; i < n; ++i) {
            ans += max(0, prices[i] - prices[i - 1]);
        }
        return ans;
    }
};
