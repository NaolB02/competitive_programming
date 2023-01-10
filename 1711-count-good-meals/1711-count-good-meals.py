class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        goodMeals = 0
        powsOfTwo = set()
        
        # contains the powers of two till 2^21
        for ind in range(22):
            powsOfTwo.add(pow(2, ind))
        
        countedDel = Counter(deliciousness)
        # holds the pairs that are already counted
        countedPairs = set()

        for mealDel in countedDel:
            for onePow in powsOfTwo:
                # checks if the meals deliciousness has a complementary in the 
                # counted deliciousness
                if onePow - mealDel in countedDel:
                    meal2Del = onePow - mealDel
                    
                    # doesn't count if the pair has already been counted
                    if mealDel != meal2Del and (mealDel, meal2Del) not in countedPairs and (meal2Del, mealDel) not in countedPairs:
                        goodMeals += (countedDel[mealDel] * countedDel[meal2Del])
                        countedPairs.add((mealDel, meal2Del))
                    
                    # checks if the deliciousness complement itself
                    elif mealDel == meal2Del:
                        if countedDel[mealDel] > 1:
                            count = countedDel[mealDel]
                            comb = factorial(count) / (factorial(count - 2) * 2)
                            goodMeals += int(comb)
        
        return goodMeals % (pow(10, 9) + 7)