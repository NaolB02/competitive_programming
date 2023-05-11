class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = Counter(words)
        frequency = [[-words[word], word] for word in words]
        heapq.heapify(frequency)
        
        out = []
        for _ in range(k):
            cur = heapq.heappop(frequency)
            out.append(cur[1])
            
        return out