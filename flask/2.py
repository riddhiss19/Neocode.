# Print message
def print_message():
    print("This is a message")


# Generate primes
def generate_primes(max_number):
    primes = []
    for num in range(2, max_number):
        if is_prime(num):
            primes.append(num)
    return primes


# Check for prime
def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
