'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 1.特判，对于数组长度 nn，如果数组为 nullnull 或者数组长度小于 33，返回 [][]。
        n = len(nums)
        if (not nums or n < 3):
            return res
        # 2.排序
        nums.sort()
        # 3.遍历排序后数组
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (nums[i] == nums[i - 1] and i > 0):
                continue
            first = i + 1
            last = n - 1
            while (first < last):
                result = nums[i] + nums[first] + nums[last]
                if (result == 0):
                    res.append([nums[i], nums[first], nums[last]])
                    while (first < last and nums[first] == nums[first + 1]):
                        first += 1
                    while (first < last and nums[last] == nums[last - 1]):
                        last -= 1
                    first += 1
                    last -= 1
                elif (result > 0):
                    last -= 1
                else:
                    first += 1

        return res


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
