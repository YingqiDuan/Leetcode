class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flattened = [num for row in mat for num in row]
        
        if r * c != len(flattened):
            return mat
        
        return [flattened[i * c:(i + 1) * c] for i in range(r)]
