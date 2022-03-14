def calc2bulbs(n_floors):
    """
    return a minimal number of needed tests
    """
    return min(i + int(n_foorls / i - 1) for i in range(1, n_floors + 1))

n = int(input("Enter the numbers of floors: "))
x = calc2bulbs(n)
print(f"{x} attempt are needed minimal")

