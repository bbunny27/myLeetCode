class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def track(nums, start, path):
            answer.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                track(nums,i+1,path)
                path.pop()
        track(nums,0,[])
        return answer
