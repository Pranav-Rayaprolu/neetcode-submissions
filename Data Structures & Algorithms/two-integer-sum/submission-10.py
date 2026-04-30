class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we should basicall find the indexes of the two elements whose sum is equal to target value
        # so this basically finding the target - given element in array. if found we return the valid index combination
        # since htis is finding values we can use a hashmap
        hashmap = {}
        # what do we store?
        # we stoer the elements as keys and their index as values
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        # now we find the elemnet 
        for i in range(len(nums)):
            if target-nums[i] in hashmap and i != hashmap.get(target-nums[i],0):
                return [i,hashmap.get(target-nums[i],0)]
        return [-1,-1]

        