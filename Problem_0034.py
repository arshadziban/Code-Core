def largest_divisible(numbers, divisor):
    divisible_numbers = [n for n in numbers if n % divisor == 0]
    return max(divisible_numbers) if divisible_numbers else -1


# Test cases
if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    divisor = int(input("Enter the divisor: "))
    
    result = largest_divisible(numbers, divisor)
    print(f"Largest number divisible by {divisor}: {result}")
