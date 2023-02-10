def unique(nums):
    a = []
    for i in nums:
        if i not in a:
            a.append(i)
    return a

print(unique(input().split()))

