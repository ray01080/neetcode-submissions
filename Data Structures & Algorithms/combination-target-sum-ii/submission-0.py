class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,cur_sum,tmp):
            if cur_sum == target:
                res.append(tmp.copy())
                return
            if cur_sum > target:# or i>=len(candidates):
                return
            for ii in range(i, len(candidates)):
                if ii > i and candidates[ii] == candidates[ii-1]:
                    continue
                tmp.append(candidates[ii])
                dfs(ii+1,cur_sum+candidates[ii],tmp)
                tmp.pop()
        dfs(0,0,[])
        return res