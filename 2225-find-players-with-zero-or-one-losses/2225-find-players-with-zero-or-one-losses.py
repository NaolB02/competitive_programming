class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lostMatches = defaultdict(int)
        answer = [[], []]
        
        for winner, loser in matches:
            lostMatches[winner]
            lostMatches[loser] += 1
        
        for player in lostMatches:
            if lostMatches[player] == 0:
                answer[0].append(player)
            
            elif lostMatches[player] == 1:
                answer[1].append(player)
        
        answer[0].sort()
        answer[1].sort()
        
        return answer