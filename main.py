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


print(basicCanSum(7, [5, 3, 4, 7]))
