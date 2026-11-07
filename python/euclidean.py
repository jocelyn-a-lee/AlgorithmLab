

def gcd(a, b):
    steps = 0
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
        steps += 1
    return abs(a), steps
if __name__ == "__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result, iterations = gcd(a, b)
    print("The GCD is:", result)
    print("Number of iterations:", iterations)
