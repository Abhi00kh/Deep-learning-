#0-1 Knapsack Problem (Dynamic Programming):
def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]
    knapsack = []

    w, v = capacity, max_value
    for i in range(n, 0, -1):
        if v <= 0:
            break
        if v == dp[i - 1][w]:
            continue
        knapsack.append(i - 1)
        w -= weights[i - 1]
        v -= values[i - 1]

    return max_value, knapsack

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, selected_items = knapsack_01(values, weights, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
