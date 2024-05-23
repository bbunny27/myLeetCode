class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def getnum(i: int) -> None:
            nonlocal ans
            if i >= len(nums):
                ans += 1
                return 
            getnum(i+1)
            if count[nums[i]+k] == 0 and count[nums[i]-k]== 0:
                count[nums[i]] += 1
                getnum(i+1)
                count[nums[i]] -= 1
        ans = -1
        count = Counter()
        getnum(0)
        return ans
# This one was particularily hard for me. I used this repo for reference. https://github.com/doocs/leetcode/blob/main/solution/2500-2599/2597.The%20Number%20of%20Beautiful%20Subsets/README_EN.md
