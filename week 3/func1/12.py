def hist(nums):
    for i in nums:
        x = i
        for j in range(x):
            print('*',end='')
        print()

hist(map(int,input().split()))
