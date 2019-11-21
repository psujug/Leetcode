'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
输入: 121
输出: true
示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or (x % 10 == 0 and x != 0)): return False
        a, b = x, 0
        while (a > b):
            b = b * 10 + a % 10
            if(a == b) : return True
            a //= 10
        return True if (a == b) else False


if __name__ == '__main__':
    print(Solution().isPalindrome(12321))
