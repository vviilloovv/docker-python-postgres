def fib(n, memo={}):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
        return memo[n]
