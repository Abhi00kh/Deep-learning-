def place(pos):
    for i in range(1, pos):
        if a[i] == a[pos] or abs(a[i] - a[pos]) == abs(i - pos):
            return False
    return True

def print_sol(n):
    global count
    count += 1
    print(f"\n\nSolution #{count}:\n")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i] == j:
                print("Q ", end="")
            else:
                print("* ", end="")
        print()

def queen(n):
    k = 1
    a[k] = 0
    while k != 0:
        a[k] = a[k] + 1
        while a[k] <= n and not place(k):
            a[k] += 1
        if a[k] <= n:
            if k == n:
                print_sol(n)
            else:
                k += 1
                a[k] = 0
        else:
            k -= 1

if __name__ == "__main__":
    n = int(input("Enter the number of Queens: "))
    a = [0] * 30
    count = 0
    queen(n)
    print(f"\nTotal solutions = {count}")
