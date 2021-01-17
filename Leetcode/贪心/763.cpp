//
//  763.cpp
//  Leetcode
//
//  Created by 刘冠中 on 2021/1/17.
//
//  字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
//  策略：先处理出字符串里里所有字母的第一次和最后一次出现位置，然后根据第一次出现位置排序，然后遍历，出现某个字母第一次出现位置大于当前最大位置则可以进行划分
//  官方题解策略：双指针+贪心  遍历两次字符串，第一次遍历保存每个字母最后出现的位置，第二次遍历仍然是出现某个字母第一次出现位置大于当前最大位置则可以进行划分

#include <vector>
#include <stdio.h>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    struct Alpha{
        int num = -1;
        int first = -1;
        int last = -1;
    };
    
    static bool comp(Alpha& a, Alpha& b){
        return a.first < b.first;
    }
    
    vector<int> partitionLabels(string S) {
        vector<int> res;
        int len = S.length();
        Alpha alphabet[26];
        for(int i = 0; i < len; i++){
            int n = S[i] - 'a';
            alphabet[n].num = n;
            if(alphabet[n].first == -1)
                alphabet[n].first = i;
            alphabet[n].last = i;
        }
        vector<Alpha> words;
        for(int i = 0; i < 26; i++){
            if(alphabet[i].num != -1)
                words.insert(words.end(), alphabet[i]);
        }
        sort(words.begin(), words.end(), comp);
        int words_len = words.size(), board = 0, prev = 0;
        for(int i = 0; i < words_len; i++){
            if(words[i].first > board){
                res.insert(res.end(), board - prev + 1);
                board = board + 1;
                prev = board;
            }
            if(words[i].last > board)
                board = words[i].last;
        }
        if(prev < len)
            res.insert(res.end(), board - prev + 1);
        
        return res;
    }
};


class Solution_official {
public:
    vector<int> partitionLabels(string S) {
        int last[26];
        int length = S.size();
        for (int i = 0; i < length; i++) {
            last[S[i] - 'a'] = i;
        }
        vector<int> partition;
        int start = 0, end = 0;
        for (int i = 0; i < length; i++) {
            end = max(end, last[S[i] - 'a']);
            if (i == end) {
                partition.insert(partition.end(), end - start + 1);
                start = end + 1;
            }
        }
        return partition;
    }
};
