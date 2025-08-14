def sum_even_fibonacci(n):
    a = 1
    b = 2
    for _ in range(n):
        fib = []
        while a < n:
            if a % 2 == 0:
                fib.append(a)
            temp_a = a
            a = b
            b = temp_a + b
        return sum(fib)

print(sum_even_fibonacci(10))
print(sum_even_fibonacci(100))
