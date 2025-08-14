def sum_squares(n):
    squares = []
    numbers = []

    for num in range(1, n + 1):
        squares.append(num ** 2)
        numbers.append(num)
    sq_of_sum = sum(numbers) ** 2
    sum_of_sq = sum(squares)
    return sq_of_sum - sum_of_sq


print(sum_squares(10))
print(sum_squares(3))