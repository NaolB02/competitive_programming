class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        counted_words = [Counter(word) for word in words]
        counted_queries = [Counter(query) for query in queries]
        ans = []
        
        for index, query in enumerate(queries):
            smallest_letter = sorted(query)[0]
            queries[index] = counted_queries[index][smallest_letter]
        
        for index, word in enumerate(words):
            smallest_letter = sorted(word)[0]
            words[index] = counted_words[index][smallest_letter]
        
        words.sort()
        
        for freq in queries:
            temp = len(words) - bisect_right(words, freq)
            ans.append(temp)
        
        return ans