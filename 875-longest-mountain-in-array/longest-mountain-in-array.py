class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        l = 0
        r = len(arr)-1
        up = 0
        down = 0
        ans = 0
        n = len(arr)
        if n<3:
            return 0
        for i in range(1,len(arr)):
            if (down > 0 and arr[i] >arr[i-1]) or arr[i] == arr[i-1] :
                up = 0
                down = 0
            if arr[i]> arr[i-1]:
                up+=1
            elif arr[i]<arr[i-1]:
                if up>0:
                    down+=1
            if up >0 and down >0:
                ans = max(ans,up+down+1)
        return ans
