def find_nth_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = find_nth_fibonacci(n - 1, memo) + find_nth_fibonacci(n - 2, memo)
        memo[n] = result
        return result

n = int(input())

if n < 0:
    print("negative numbers.")
else:
    nth_fibonacci = find_nth_fibonacci(n)
    print(nth_fibonacci)
