'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if (not nums and n < 3):
            return None
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n):
            first = i + 1
            last = n - 1
            while (first < last):
                res = nums[i] + nums[first] + nums[last]
                print(res,i,first,last)
                if (target == res):
                    return target
                if (abs(target - res) < abs(target - ans)):
                    ans = res
                if (res > target):
                    last -= 1
                else:
                    first += 1

        return ans


if __name__ == '__main__':
    print(Solution().threeSumClosest([-3,-2,-5,3,-4], -1))
