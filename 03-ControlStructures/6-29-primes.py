"""
A natural number greater than 1 is called a prime if it has exactly 2 natural factors with the values 1 and this number.
The program finds N leading prime numbers. Read the value of N from the keyboard. Using loop statements checks that the
 number N is divisible only by 1 and by N.
"""

max_primes = int(input("Provide the number of primes to display: "))
primes_found = 0
n = 2

while primes_found < max_primes:
    factors_cnt = 0
    for i in range(2, n):  # divide by numbers from 2 to n-1
        if n % i == 0:
          factors_cnt += 1

    if factors_cnt == 0:
        print(n, end=' ')
        primes_found += 1
    n += 1