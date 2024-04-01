---
CTF: UTCTF'24
Category: crypto
Points: 673
Date: 2024-03-31
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
utflag{deep_seated_and_recurring_self-doubts}
```

### Details

Description

> I wrote an amazing encryption service. It is definitely flawless, so I'll encrypt the flag and give it to you.
> 
> By jocelyn (@jocelyn3270 on discord)


Files
main.py

```python
seed = random.randint(0, 10 ** 6)
def get_random_number():
    global seed 
    seed = int(str(seed * seed).zfill(12)[3:9])
    return seed

def encrypt(message):
    key = b''
    for i in range(8):
        key += (get_random_number() % (2 ** 16)).to_bytes(2, 'big')
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext.hex()
```

From the program we can get encrypted flag or encrypt our message. So, basically, we need to guess the seed 

```python
def solve():
    ciphertext_hex = "d6c1b283f0a3c1abd7b8b03ada8c469b10710a08c7bc9ae7dbe8cbc9a184821e8a8340b0e50b5377a0eef1d8315a135c"
    for seed in range(0, 10 ** 6):
        try:
            decrypted_message = decrypt(ciphertext_hex, seed)
            print(f"Decrypted message with seed {seed}: {decrypted_message.decode()}")
            break
        except ValueError:
            continue
```

Running it we get the flag (keep in mind, that seed is randomly generated every time )

![](assets/Pasted%20image%2020240331001918.png)

Flag:
```
utflag{deep_seated_and_recurring_self-doubts}
```



---
### Appendix


solve.py
```python
#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def get_random_number(seed):
    """Replicates the pseudo-random number generation from the given seed."""
    seed = int(str(seed * seed).zfill(12)[3:9])
    return seed

def decrypt(ciphertext_hex, seed):
    """Attempts to decrypt the given ciphertext using the AES key generated from the seed."""
    key = b''
    for i in range(8):
        seed = get_random_number(seed)
        key += (seed % (2 ** 16)).to_bytes(2, 'big')
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = bytes.fromhex(ciphertext_hex)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext


def solve():
    ciphertext_hex = "6bf2f013fd2100d9b2bbc17e43f3c60b94d6b64a41e4d7506c756b7a3a6e7141532e9162076bd7c146d8770bb1ea4d09"
    for seed in range(0, 10 ** 6):
        try:
            decrypted_message = decrypt(ciphertext_hex, seed)
            print(f"Decrypted message with seed {seed}: {decrypted_message.decode()}")
            break
        except ValueError:
            continue


if __name__ == "__main__":
    solve()

```