def numbers_with_divisors_three(n):

    li = []
    i = 2
    while i * i <= n:
        if (isPrime(i)):
            if (i * i <= n):

                li.append(i)

        i += 1

    print(len(li))

def isPrime(n):
    if (n == 0 or n == 1):
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False

        i += 1

    return True

j = 10

numbers_with_divisors_three(j)
