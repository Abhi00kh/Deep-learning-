#0-1 Knapsack Problem (Dynamic Programming):
def knapsack(values ,weights,capacity):
    n =len(values)
    dp=[0]*(capacity+1)

    for i in range(n):
        for w in range(capacity , weights[i]-1,-1):
            dp[w]=max(dp[w], dp[w-weights[i]]+values[i])
    return dp[capacity]   
values =  [60,10,120]
weights =[10,20,30]
capacity =50
max_value =  knapsack(values ,weights,capacity)
print (max_value)