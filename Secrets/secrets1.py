import secrets

# secrets module is used for cryptographically secure random values
# (used in passwords, tokens, OTPs, session IDs)

# randbelow(n) returns a secure random integer from 0 to n-1
print(secrets.randbelow(10))

# choice(sequence) selects a secure random element from a sequence
mylist = list("ABCDEFGH")
print(secrets.choice(mylist))

# token_hex(n) generates a secure random hex string (2*n characters)
# commonly used for API keys and secret tokens
print(secrets.token_hex(16))

# token_urlsafe(n) generates a URL-safe random string
# useful for links, reset tokens, session IDs
print(secrets.token_urlsafe(16))

import string

# creating a character set for password generation
alphabet = string.ascii_letters + string.digits + "!@#$%^&*"

# generating a secure random password of length 12
password = ''.join(secrets.choice(alphabet) for _ in range(12))
print(password)