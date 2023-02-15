class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        playerPt, trainerPt = 0, 0
        pairs = 0
        players.sort()
        trainers.sort()
        
        
        while playerPt < len(players) and trainerPt < len(trainers):
            if players[playerPt] > trainers[trainerPt]:
                trainerPt += 1
            
            else:
                trainerPt += 1
                playerPt += 1
                pairs += 1
        
        return pairs