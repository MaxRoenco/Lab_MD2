import random
import math

m = input("Input message: ")
p = 0
q = 0


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    else:
        return True


while not is_prime(q):
    q = random.randrange(2, 100000)
while not is_prime(p):
    p = random.randrange(2, 100000)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


n = p * q
phi = (p - 1) * (q - 1)

e = random.randrange(1, phi)
if gcd(e, phi) != 1:
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

cipher_text = [pow(ord(char), e, n) for char in m]

# Calculate the modular multiplicative inverse of 'e' modulo 'phi'
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

d = mod_inverse(e, phi)
print(cipher_text)
decrypted_text = [pow(num, d, n) for num in cipher_text]
decrypted_message = ''.join(chr(char) for char in decrypted_text)

print("Decrypted Message:", decrypted_message)
