import math
def check_prime(number):
    sqrt_num = math.sqrt(number)
    for i in range(2, len(str(sqrt_num)) + 1):
        if (number / i).is_integer():
            return False
        return True

if __name__ == "__main__":
    print(f"check_prime(10,000,000) = {check_prime(10_000_000)}")
    print(f"check_prime(10,000,019) = {check_prime(10_000_019)}")
