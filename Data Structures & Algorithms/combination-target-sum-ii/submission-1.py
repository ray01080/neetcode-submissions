class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            for x in range(i,len(candidates)):
                if x > i and candidates[x] == candidates[x-1]:
                    continue
                cur.append(candidates[x])
                dfs(x+1, cur, total+candidates[x])
                cur.pop()
        dfs(0,[],0)
        return res