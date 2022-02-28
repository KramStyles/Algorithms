def findMaxConsecutiveOnes(nums):
        counter = 0
        checks = []
        for x, y in enumerate(nums):
            if (x + 1) < len(nums): 
                if y == 1 and nums[x+1] == 1:
                    counter += 1
                elif x > 0 and (y==1 and nums[x-1] == 1):
                    counter +=1
                elif y == 1 and x == 0:
                    counter +=1
                else:
                    checks.append(counter)
                    counter = 0
            elif y == 1: 
                counter += 1
        checks.append(counter)
        
        return (max(checks))

# test = [1,0,1,1,0,1]
test = [1,0]
test1 = [1,0,1,1,1]

print(findMaxConsecutiveOnes(test))
# print(findMaxConsecutiveOnes(test1))