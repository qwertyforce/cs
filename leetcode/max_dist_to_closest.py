class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        pre_zeros=-1
        max_in_between_zeros=-1
        post_zeros=-1
        zeros=0
        for seat in seats:
            if seat==0:
                zeros+=1
            else:
                if pre_zeros==-1:
                    pre_zeros=zeros
                else:
                    max_in_between_zeros = max(max_in_between_zeros, zeros)
                zeros=0
        post_zeros = zeros
        return max(pre_zeros, post_zeros, (max_in_between_zeros + 1) // 2)