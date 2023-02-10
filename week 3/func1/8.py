def spy_game(nums):
    for i in range(len(nums)):
        if i == len(nums)-1:
            return False
        if nums[i] == 0:
            for a in range(i+1,len(nums)):
                if a == len(nums)-1:
                    return False
                if nums[i] == 0:
                    for x in range(a+1,len(nums)):
                        if nums[x] == 7:
                            return True
                        if x == len(nums)-1:
                            return False


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))