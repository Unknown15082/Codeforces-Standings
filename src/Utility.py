from hashlib import sha512
from random import randint

def hash(s):
    return sha512(s.encode()).hexdigest()

def randstring(n, s):
    res = ""
    for _ in range(n):
        res += s[randint(0, len(s) - 1)]
    return res

if __name__ == "__main__":
    pass