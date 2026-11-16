class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = len(nums) * [False]
        tmp = []
        def dfs():
            if len(nums) == len(tmp):
                res.append(tmp.copy())
                return
            for i in range(len(nums)):
                if not(used[i]):
                    tmp.append(nums[i])
                    used[i] = True
                    dfs()
                    tmp.pop()
                    used[i] = False
        dfs()
        return res