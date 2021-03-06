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


def gridTravellerTable(m, n):
    table = [[0 for _ in range(n+1)] for _ in range(m + 1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if j + 1 <= n:
                table[i][j + 1] += current
            if i + 1 <= m:
                table[i+1][j] += current
    return table[m][n]


def hourglassSum(arr):
    # Write your code here
    def getHourGlassSum(arr, i, j):
        return arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

    sumOfHourGlass = []
    for i in range(6):
        for j in range(6):
            if i + 2 <= 5 and j+2 <= 5:
                sumOfHourGlass.append(getHourGlassSum(arr, i, j))
    return max(sumOfHourGlass)


myArr = [[1, 1, 1, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]
         ]

print(hourGlass(myArr))


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
