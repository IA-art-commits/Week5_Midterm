import hashlib
import hmac

# Read original data
with open("data.txt", "rb") as f:
    data = f.read()

print("Original data:", data.decode().strip())

# --- Task 3A: SHA-256 hash ---
sha256_hash = hashlib.sha256(data).hexdigest()
print("SHA-256 hash of data.txt:", sha256_hash)

# --- Task 3B: HMAC using SHA-256 ---
key = b"secretkey123"
hmac_value = hmac.new(key, data, hashlib.sha256).hexdigest()
print("HMAC-SHA256 of data.txt with key 'secretkey123':", hmac_value)
