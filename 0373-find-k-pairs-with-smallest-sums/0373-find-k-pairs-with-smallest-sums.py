class Solution:
    def inbound(self, i, j, n1, n2):
        return 0 <= i < n1 and 0 <= j < n2
    
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0] + nums2[0], 0, 0)]
        pairs = []
        visited = set((0, 0))
        count = 0
        
        while heap and count < k:
            summ, i, j = heapq.heappop(heap)
            
            pairs.append([nums1[i], nums2[j]])
            visited.add((i, j))

            
            if (i + 1, j) not in visited and self.inbound(i + 1, j, len(nums1), len(nums2)):
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            
            if (i, j + 1) not in visited and self.inbound(i, j + 1, len(nums1), len(nums2)):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            
            count += 1
            
        return pairs