n = int(input("Check this number: "))


def prime_checker(number=n):
    is_prime = True
    for x in range(2, number):
      if number % x == 0:
        is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's a not prime number.")

prime_checker()