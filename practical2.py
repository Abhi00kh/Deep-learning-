class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def fractionalKnapsack(W, items):
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    total_value = 0
    for item in items:
        if W >= item.weight:
            total_value += item.value
            W -= item.weight
        else:
            total_value += (W / item.weight) * item.value
            break
    return total_value


# Example usage
W = 50
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
max_value = fractionalKnapsack(W, items)
print("Maximum value in the knapsack:", max_value)
