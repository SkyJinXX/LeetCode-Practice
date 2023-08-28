def max_chocolates(num_jars, jars):
    if num_jars == 1:
        return jars[0]
    elif num_jars == 2:
        return max(jars)
    elif num_jars == 3:
        return max(jars[0] + jars[2], jars[1])

    dp = [-1] * num_jars
    dp[0], dp[1], dp[2] = jars[0], jars[1], jars[2] + jars[0]
    for i in range(3, num_jars):
        dp[i] = max(dp[i - 2], dp[i - 3]) + jars[i]
    
    return max(dp[-1], dp[-2])


if __name__ == "__main__":
    # num_jars = 6
    # jars = [5, 30, 99, 60, 5, 10]
    num_jars = int(input().strip())
    jars = list(map(int, input().split()))
    result = max_chocolates(num_jars, jars)
    print(result)
