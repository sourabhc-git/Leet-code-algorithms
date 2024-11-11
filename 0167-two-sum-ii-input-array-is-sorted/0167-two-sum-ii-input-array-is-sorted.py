class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #dict1 = {}
        #for i  in range(0, len(numbers)):
        #
        #    complement  = target - numbers[i]
        #    if complement not in dict1:
        #        dict1[numbers[i]] = i
        #    else:
        #        return [dict1[complement]+1, i+1]
            
        
        start = 0
        
        end = len(numbers) - 1
        
        while start < end:
            
            sum_ = numbers[start] + numbers[end]
            
            if sum_ == target:
                return [start+1, end+1]
            elif sum_ > target:
                end -=1
            elif sum_ < target:
                start +=1


        