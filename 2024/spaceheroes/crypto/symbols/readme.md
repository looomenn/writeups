---
CTF: spaceheroes'24
Category: crypto
Points: "100"
Date: 2024-04-13
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
shctf{th1s_was_ju5t_a_big_d1str4ction}
```

### Details

Description

> We have reason to believe that Mortimer is rebuilding the Armageddon Machine. We managed to intercept a message sent from his personal computer. After consulting with the Oracle, we were only able to discover two things:
> 
> The tool used to encrypt messages (encrypt.py)
> All messages sent by Mortimer begin with Mortimer_McMire:
> 
> Can you decrypt the message?

Files
- encrypt.py
- message.enc


solve.py

```python
#!/usr/bin/env python3

from Crypto.Cipher import AES
import binascii

key = b"3153153153153153"
encrypted_message_hex = "2a21c725b4c3a33f151be9dc694cb1cfd06ef74a3eccbf28e506bf22e8346998952895b6b35c8faa68fac52ed796694f62840c51884666321004535834dd16b1"
encrypted_message = binascii.unhexlify(encrypted_message_hex)

known_plaintext = b"Mortimer_McMire:"

cipher = AES.new(key, AES.MODE_CBC, b'\x00' * 16)
dummy_encrypted_block = cipher.encrypt(known_plaintext)

real_iv = bytes([_a ^ _b for _a, _b in zip(dummy_encrypted_block, encrypted_message[:16])])

cipher = AES.new(key, AES.MODE_CBC, real_iv)

decrypted_message = cipher.decrypt(encrypted_message)

print("Decrypted message:", decrypted_message)

```

```
Decrypted message: b'dC\xf8\x97\r\x97\xd5$\xc7\xaf_\xb9\x1epK\x91          shctf{th1s_was_ju5t_a_big_d1str4ction}'
```

