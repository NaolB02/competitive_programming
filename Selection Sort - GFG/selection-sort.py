#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        min_pos = i
        for counter in range(i, len(arr)):
            if arr[counter] < arr[min_pos]:
                min_pos = counter
        
        return min_pos
    
    def selectionSort(self, arr,n):
        #code here
        i = 0
        while i < n:
            new_pos = self.select(arr, i)
            arr[i], arr[new_pos] = arr[new_pos], arr[i]
            i += 1
            
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends