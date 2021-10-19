class Solution:

    # 自己的第一種解法，別人跑很快，我寫就105ms
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        for num in nums1:
            if num in nums2:
                nums.append(num)
                nums2.remove(num)
        return nums
    
    # 第二種，邏輯優化後的第一種，但還是比別人家的第一種64ms慢
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = 0
        while count < len(nums1):
            if nums1[count] in nums2:
                nums2.remove(nums1[count])
                count += 1
            else:
                nums1.remove(nums1[count])
        return nums1
        
    # 看完學起來的最佳解
    # 註解還開嘲諷，time: O(m+n)
    # 重點是利用 collections.Counter 這個之前沒聽說的東西
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # time: O(m+n), space: O(m+n)
        counts = collections.Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return res