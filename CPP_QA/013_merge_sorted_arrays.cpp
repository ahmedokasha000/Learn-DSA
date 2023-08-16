#include <iostream>
#include <vector>
#include <algorithm>
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int n2_cur_index = n - 1; 
        int n1_cur_index = m -1;
        for (int next_big_val_ind = static_cast<int>(nums1.size()) - 1; n2_cur_index >= 0; --next_big_val_ind){
            if (n1_cur_index < 0 || nums2[n2_cur_index] > nums1[n1_cur_index]) {
                nums1[next_big_val_ind] = nums2[n2_cur_index];
                n2_cur_index--;
            } else {
                nums1[next_big_val_ind] = nums1[n1_cur_index];
                n1_cur_index--;
            }
        }
    }
};