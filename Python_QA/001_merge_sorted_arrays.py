
from typing import List


class Solution:
    def __init__(self):
        pass

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums2_cur_index = n-1
        nums1_cur_index = m-1
        next_biggest_index = len(nums1)-1
        while nums2_cur_index >= 0 :
            if nums1_cur_index < 0 or nums2[nums2_cur_index] > nums1[nums1_cur_index]:
                nums1[next_biggest_index] = nums2[nums2_cur_index]
                nums2_cur_index -= 1 
            else:
                nums1[next_biggest_index] = nums1[nums1_cur_index]
                nums1_cur_index -= 1
            next_biggest_index -= 1
        return nums1
    
    def shift_right(self, nums, start_index, end_index):
        for i in range(end_index, start_index, -1):
            nums[i] = nums[i-1]
        return nums


def test_merge_sorted_lists():
    sol = Solution()
    l1 = [1,2,3,0,0,0]
    l2 = [2,5,6]
    res = sol.merge(l1, 3, l2, 3)
    print(res)
    pass

def main():
    test_merge_sorted_lists()
    
if __name__ == "__main__":
    main()