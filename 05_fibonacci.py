n = int(input("Enter the number of Fibonacci terms: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    a, b = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    print("Fibonacci sequence:")
    print(*sequence)
