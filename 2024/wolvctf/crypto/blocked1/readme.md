---
CTF: WolvCTF'24
Category: crypto
Points: "100"
Date: 
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
wctf{th3y_l0st_th3_f1rst_16_byt35_0f_th3_m3ss4g3_t00}
```

### Details

Description

> The WOLPHV group (yes, this is an actual article) group encrypted our files, but then blocked us for some reason. I think they might have lost the key. Let's log into their accounts and find it...


Files
- nc server ip

Known plaintext AES bitflip attack using [AES-flipper](https://github.com/Vozec/AES-Flipper)

![](assets/Pasted%20image%2020240507135648.png)

solve.py

```python
#!/usr/bin/env python3

from AES_flipper import Aesflipper
from pwn import *

def solve():
    con = process('python3 ./server.py', shell=True)
    con.recvuntil(b'you are logged in as: ')
    
    username = con.recvline().strip()

    print(f'[*] Logged as: {username.decode()}')

    plain = b'password reset: ' + username
    target = b'password reset: doubledelete'

    print(f'[*] Payload: {plain}')

    con.recvuntil(b'> ')
    con.sendline(b'2')
    token = bytes(con.recvline().decode().strip(), 'utf-8')

    print(f'[*] {token=}')

    print(f'[&] AES Flipper init...')

    flipper = Aesflipper(
        plain=plain,
        ciphertext=token,
        add_iv=True,
        debug=True
    )

    new_token = flipper.full_flip(target=target)
    
    print(f'[*] New token: {token}')

    con.recvuntil(b'> ')
    con.sendline(b'1')
    con.sendline(new_token)

    con.recvuntil(b'doubledelete\n')
    
    print('flag:\n')
    print(con.recvline().decode().strip())

    con.close()

if __name__ == "__main__":
    solve()

```