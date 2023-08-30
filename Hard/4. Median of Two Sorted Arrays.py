class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res_lst = sorted(nums1 + nums2)
        res_lenght = len(res_lst)
        if res_lenght % 2 == 0:
            med_ind = int(res_lenght / 2) - 1
            next_ind = med_ind + 1
            median = (res_lst[med_ind] + res_lst[next_ind]) / 2
            return median
        else:
            med_ind = res_lenght // 2
            median = float(res_lst[med_ind])
            return median