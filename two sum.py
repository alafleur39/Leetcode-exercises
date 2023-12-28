class Solution(object): 
    def twoSum(self, nums, target): #Target = 6
        #empty_nums = []
        for i in range(len(nums)): # nested for loop 
            for x in range(i+1,len(nums)): # we did this to get the starting point in our index to 1    #x is at least greater by 1 i = [0], x = [1]
                if nums[i] + nums[x] == target: # if the indexes add up to our target they return the index that sums up to that target
                    return i, x
            #if nums[i] + nums[i+1] == target:
                #return i, i+1
            #nums[0] -> nums[1] nums[2] nums[3]....
            


self1 =  None            
nums1 = [3,2,5,4]
test_target = 6

result=Solution.twoSum(self1,nums1,test_target) # this is how we test our function
print(result) # this is how we print our  result
