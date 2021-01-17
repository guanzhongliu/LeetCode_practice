//
//  main.cpp
//  Leetcode
//
//  Created by 刘冠中 on 2021/1/16.
//

#include <iostream>

#include "贪心/763.cpp"
using namespace std;

int main() {
    Solution solution;
    string s = "aaacbbb";
    vector<int> ans = solution.partitionLabels(s);
    int a = ans.size();
    for(int i = 0; i < a; i++)
    cout << ans[i] << ' ';
    return 0;
}
