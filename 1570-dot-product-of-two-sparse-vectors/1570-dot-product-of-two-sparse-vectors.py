class SparseVector:
    def __init__(self, nums: List[int]):
        self.data = {i: num for i,num in enumerate(nums) if num}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if len(self.data) < len(vec.data):
            shorter = self.data
            longer = vec.data
        else:
            shorter = vec.data
            longer = self.data
        
        return sum(shorter[i] * longer.get(i,0) for i in shorter)

    
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)