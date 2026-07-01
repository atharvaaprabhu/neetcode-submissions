class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        i =0
        j=length-1
        maxi = 0
        while j>i :
            mini = min(heights[i],heights[j])
            print("mini: ",mini)
            gap = j-i
            print("gap",gap)
            area = mini*gap
            print("area",area)
            if maxi<area :
                maxi = area
            if (heights[i] > heights[j]) :
                j -= 1
            else :
                i+= 1
        return maxi