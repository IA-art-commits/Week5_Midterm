import secrets

# Public parameters (for demonstration)
p = 23  # prime modulus
g = 5   # generator

print(f"Public parameters: p = {p}, g = {g}")

# Alice chooses private key a
a = secrets.randbelow(p - 2) + 1

# Bob chooses private key b
b = secrets.randbelow(p - 2) + 1

print(f"Alice's private key (a): {a}")
print(f"Bob's private key (b): {b}")

# Compute public keys
A = pow(g, a, p)
B = pow(g, b, p)

print(f"Alice's public key (A = g^a mod p): {A}")
print(f"Bob's public key (B = g^b mod p): {B}")

# Compute shared secret
shared_secret_alice = pow(B, a, p)
shared_secret_bob   = pow(A, b, p)

print(f"Shared secret computed by Alice: {shared_secret_alice}")
print(f"Shared secret computed by Bob:   {shared_secret_bob}")

print("Keys equal?", shared_secret_alice == shared_secret_bob)
