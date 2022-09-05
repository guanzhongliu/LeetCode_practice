//
//  605.cpp
//  Leetcode
//
//  Created by 刘冠中 on 2021/1/16.
//
//  假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
//  给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。
//  策略：扫一遍，计算各种情况下空地可以种多少（skip思路更好，官方题解代码更简洁，附在后面）

#include <vector>
#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <math.h>

using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int len = flowerbed.size();
        int i = 0, emp = 0, last = 0;
        while(n > 0 && i < len){
            if(flowerbed[i] != 1){  // 是空地
                emp++;
            }
            else if(last == 1){   // 左右侧有花
                n -= floor((emp - 2)/2.0 + 0.5);
                emp = 0;
                last = 1;
            }
            else{   // 左侧无花
                n -= floor(emp/2.0);
                emp = 0;
                last = 1;
            }
            
            i++;
        }
        if(emp != 0){
            if(last == 0)   // 左右都无花
                n -= floor(emp/2.0);
            else    // 右侧无花
                n -= floor(emp/2.0);
        }
        
        return n <= 0;
    }
};

// 如果当前格子是1则下一格子一定是0
class Solution_skip {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // 每次跳两格
         for (int i = 0; i < flowerbed.size(); i += 2) {
             // 如果当前为空地
            if (flowerbed[i] == 0) {
                // 如果是最后一格或者下一格为空
                if (i == flowerbed.size() - 1 || flowerbed[i + 1] == 0) {
                    n--;
                } else {
                    i++;
                }
            }
        }
        return n <= 0;
    }
};

class Solution_official {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int count = 0;
        int m = flowerbed.size();
        int prev = -1;
        for (int i = 0; i < m; i++) {
            if (flowerbed[i] == 1) {
                if (prev < 0) {
                    count += i / 2;
                } else {
                    count += (i - prev - 2) / 2;
                }
                if (count >= n) {
                    return true;
                }
                prev = i;
            }
        }
        if (prev < 0) {
            count += (m + 1) / 2;
        } else {
            count += (m - prev - 1) / 2;
        }
        return count >= n;
    }
};
