def fibonacci(nterms):
    n1 = 0
    n2 = 1
    count = 0
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci to", nterms, "is:")
        print(n1)
    else:
        print("Fibonacci sequence to", nterms, "is:")
        while count < nterms:
            print(n1, end=' , ')
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

print(fibonacci(1))


