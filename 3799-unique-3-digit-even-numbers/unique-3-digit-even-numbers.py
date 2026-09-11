class Solution:
    def totalNumbers(self, nums: List[int]) -> int:
        mp = [0]*10
        res = []
        for x in nums:
            mp[x]+=1
        for i in range(1,10):
            if mp[i] == 0:
                continue
            mp[i]-=1
            for j in range(10):
                if mp[j] == 0:
                    continue
                mp[j] -= 1
                for k in range(0,10,2):
                    if mp[k] == 0:
                        continue
                    res.append(i*100+j*10+k)
                mp[j]+=1
            mp[i]+=1
        return len(res)


        