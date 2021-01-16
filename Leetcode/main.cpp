//
//  main.cpp
//  Leetcode
//
//  Created by 刘冠中 on 2021/1/16.
//

#include <iostream>

#include "贪心/605.cpp"
using namespace std;

int main() {
    Solution solution;
    vector<int> a;
//    a.insert(a.end(), 0);
//    a.insert(a.end(), 0);
    a.insert(a.end(), 0);
    a.insert(a.end(), 0);
    a.insert(a.end(), 1);
    a.insert(a.end(), 0);
    a.insert(a.end(), 1);
//    a.insert(a.end(), 0);
//    a.insert(a.end(), 0);
//    a.insert(a.end(), 0);
    cout << solution.canPlaceFlowers(a, 1) << endl;
}
