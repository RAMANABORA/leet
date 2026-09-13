class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a=[];b=[]
        n=len(img1);m=len(img1[0])
        for i in range(n):
            for j in range(m):
                if img1[i][j]==1:
                    a.append((i,j))
                if img2[i][j]==1:
                    b.append((i,j))
        d={}
        for i,j in a:
            for x,y in b:
                p,q=x-i,y-j
                if (p,q) not in d:
                    d[(p,q)]=0
                d[(p,q)]+=1
        if not d:
            return 0
        return max(d.values())