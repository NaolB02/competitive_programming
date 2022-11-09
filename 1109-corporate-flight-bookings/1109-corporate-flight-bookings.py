class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * (n + 1)
        out = [0] * n
        
        for first, end, seat in bookings:
            seats[first - 1] += seat
            seats[end] -= seat
        
        out[0] = seats[0]
        for i in range(1, len(seats) - 1):
            out[i] = out[i - 1] + seats[i]
            
        return out