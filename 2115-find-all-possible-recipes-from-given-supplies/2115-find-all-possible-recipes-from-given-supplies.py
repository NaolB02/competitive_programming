class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {x: [] for x in recipes}
        dependencies = {x: 0 for x in recipes}
        supplies = set(supplies)
        
        for i, recipe in enumerate(recipes):
            for ingr in ingredients[i]:
                if ingr not in supplies and ingr in graph:
                    graph[ingr].append(recipe)
                    dependencies[recipe] += 1
                
                elif ingr not in supplies and ingr not in graph:
                    dependencies[recipe] += 1
        
        frontier = deque()
        for recipe in dependencies:
            if dependencies[recipe] == 0:
                frontier.append(recipe)
        
        createable = []
        
        while frontier:
            parent = frontier.popleft()
            
            for child in graph[parent]:
                dependencies[child] -= 1
                
                if dependencies[child] == 0:
                    frontier.append(child)
            
            createable.append(parent)
        
        return createable