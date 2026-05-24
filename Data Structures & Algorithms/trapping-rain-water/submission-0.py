class Solution:
    def trap(self, height: List[int]) -> int:
        l,lmax,rmax,result=0,0,0,0
        n=len(height)
        r=n-1
        while l<r:
            lmax=max(lmax,height[l])
            rmax=max(rmax,height[r])
            if lmax<rmax:
                result+=lmax-height[l]
                l+=1
            else:
                result+=rmax-height[r]
                r-=1
        return result

        