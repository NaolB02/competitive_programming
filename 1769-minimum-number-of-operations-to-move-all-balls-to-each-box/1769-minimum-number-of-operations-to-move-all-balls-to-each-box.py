class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)
        
        for index in range(len(boxes)):
            for index2 in range(len(boxes)):
                if index == index2:
                    continue
                    
                if boxes[index2] == "1":
                    answer[index] += abs(index2 - index)
        
        return answer