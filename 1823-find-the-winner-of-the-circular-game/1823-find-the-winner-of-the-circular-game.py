class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [player for player in range(1, n + 1)]
        curInd = 0
        k = k - 1
        
        while len(players) > 1:
            curInd += k
            curInd %= n
            players.pop(curInd)
            n = len(players)
            
        return players[0]