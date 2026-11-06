class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        c = 0
        people.sort()
        l , r = 0 , len(people)-1
        while l<=r:
            if people[l]+people[r] <= limit:
                l+=1
            c+=1
            r-=1
        return c
            
        