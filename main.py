# memoized recursive solution for grid traveller problem
def gridTraveller(m, n, memo={}):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    memo[key] = gridTraveller(m-1, n) + gridTraveller(m, n-1)
    return memo[key]


def basicCanSum(n, m):
    hashmap = {}
    for i in m:
        if i in hashmap:
            return True
        hashmap[n-i] = True


# print(basicCanSum(7, [5, 3, 4, 7]))


"""
fib tabulation
n = 6
 0  1  2  3  4  5  6
[0, 1, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 3, 5, ]
"""


def fibTable(n):
    table = [0 for _ in range(n+1)]
    table[1] = 1
    for index, val in enumerate(table):
        if index + 1 <= n:
            table[index + 1] += val
        if index + 2 <= n:
            table[index + 2] += val
    print(table)
    return table[n]


print(fibTable(5))


def search(nums, target):
    middle = len(nums)//2
    while middle >= 0:
        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            nums = nums[middle:]
        if nums[middle] > target:
            nums = nums[:middle]
        middle = len(nums)//2
    return -1
