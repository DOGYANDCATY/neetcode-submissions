class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1

        dic = {}
        k = 0
        for char in nums:
            if char in dic:
                dic[char] = [dic[char], k]
            else:
                dic[char] = k
            k+=1

        nums.sort()

        while i != j:
            s = nums[i] + nums[j]
            if s == target:
                if nums[i] != nums[j]:
                    ans = [dic[nums[i]], dic[nums[j]]]
                else:
                    ans = [dic[nums[i]][0], dic[nums[j]][1]]
                return sorted(ans)
            elif s < target:
                i+=1
            elif s > target:
                j-=1