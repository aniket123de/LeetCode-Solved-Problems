class Solution:
    def checkRecord(self, s: str) -> bool:
        total_a = 0
        consecutive_l = 0
        
        for char in s:
            if char == 'A':
                total_a += 1
                consecutive_l = 0
            elif char == 'L':
                consecutive_l += 1
            else:  # char == 'P'
                consecutive_l = 0
            
            if total_a >= 2 or consecutive_l >= 3:
                return False
        
        return True