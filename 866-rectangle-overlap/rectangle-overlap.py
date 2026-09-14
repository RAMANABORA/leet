class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        l = max(rec1[0],rec2[0])
        r = min(rec1[2],rec2[2])
        b = max(rec1[1],rec2[1])
        t = min(rec1[3],rec2[3])
        wid = r-l 
        hig = t-b
        return wid>0 and hig>0
        