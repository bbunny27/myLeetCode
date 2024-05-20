class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        answer, n = 0, len(nums)
        for i in range (1 << n):
            b = 0
            for k in range (n):
                if i >> k & 1:
                    b ^= nums[k]
            answer += b
        return answer