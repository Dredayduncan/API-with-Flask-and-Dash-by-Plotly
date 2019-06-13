def fibonacci(nterms):
    first = 0
    second = 1
    count = 0
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci to", nterms, "is:")
        print(first)
    else:
        print("Fibonacci sequence to", nterms, "is:")
        while count < nterms:
            print(first, end=' , ')
            nth = first + second
            first = second
            second = nth
            count += 1

print(fibonacci(6))


