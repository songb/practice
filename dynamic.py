def lengthOfLIS(nums):
    counter = []
    for i in range(len(nums)):
        m = find_small_max(nums, counter, i, nums[i]) + 1
        counter.append(m)
    if counter:
        return max(counter)
    else:
        return 0


def find_small_max(nums, counter, index, current):
    max_number = 0
    for i in range(index):
        if nums[i] < current:
            max_number = max(max_number, counter[i])
    return max_number


def maxProfit(prices):
    profit = [0]
    for i in range(1, len(prices)):
        profit.append(find_max(prices, profit, prices[i], i))

    return max(profit)


def find_max(prices, profit, current, index):
    max_p = 0
    for i in range(index):
        if current > prices[i]:
            max_p = max(max_p, profit[i] + current - prices[i])
    return max_p


def maxSubArray(nums):
    max_num = nums[0]
    current = nums[0]
    for n in nums[1:]:
        if n > current and 0 >= current:
            current = n
            max_num = max(max_num, current)
        elif n > 0:
            current = current + n
            max_num = max(max_num, current)
        else:
            current = current+n

    return max(max_num, current)


m = maxSubArray([-1,-2])

print(m)
