class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for i in range(len(arr1)):
            flag = True
            for j in range(len(arr2)):
                k = abs(arr1[i] - arr2[j])
                if k <= d:
                    flag = False
            if flag == True:
                count+=1
            

        return count

                

                