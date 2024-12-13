class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        cars = sorted(zip(position, speed), reverse = True)
        for pos,sp in cars:
            time.append(((target - pos) / sp))
        
        curr = 0 
        result = 0
        for j in time:
            if j > curr:
                result = result + 1
                curr = j
        
        return result
            
        