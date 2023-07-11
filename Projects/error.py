def sum_of_divisors(number):
    if number <= 0:
        return 0

    divisors_sum = 0

    for i in range(1, number + 1):
        if number % i == 0:
            divisors_sum += i

    return divisors_sum

# Example usage
num = 6
divisors_sum = sum_of_divisors(num)
print("Sum of divisors of", num, "is", divisors_sum)
