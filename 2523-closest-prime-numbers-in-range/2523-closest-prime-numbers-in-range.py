class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = self.prime_sieve(right)
        
        nums = []
        for i in range(left, right + 1):
            if is_prime[i]:
                nums.append(i)
        
        if len(nums) < 2:
            return [-1, -1]
        
        min_diff = math.inf
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] < min_diff:
                min_diff = nums[i] - nums[i - 1]
                min_pairs = [nums[i - 1], nums[i]]
        
        return min_pairs
    
    def prime_sieve(self, n: int) -> list[bool]:
        is_prime: list[bool] = [True for _ in range(n + 1)]
        is_prime[0] = is_prime[1] = False

        i = 2

        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j <= n:
                    is_prime[j] = False
                    j += i
            i += 1

        return is_prime

