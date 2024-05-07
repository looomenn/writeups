---
CTF: WolvCTF'24
Category: crypto
Points: "100"
Date: 2024-03-16
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
wctf{X0R_i5_f0rEv3r_My_L0Ve}
```

### Details

Description

> I have encrypted some text but it seems I have lost the key! Can you find it?
> 

Files
- [yors-truly.py](https://github.com/WolvSec/WolvCTF-2024-Challenges-Public/blob/master/beginner/crypto/yors-truly/challenge/yors-truly.py "yors-truly.py")

solve.py

```python
#!/usr/bin/env python3 

import base64

CYPHER = "NkMHEgkxXjV/BlN/ElUKMVZQEzFtGzpsVTgGDw=="
PLAINT = "A string of text can be encrypted by applying the bitwise XOR operator to every character using a given key"

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


def solve() -> None:
    
    decoded = base64.b64decode(CYPHER)
    key = byte_xor(decoded, PLAINT.encode())
    print(key)


if __name__ == "__main__":
    solve()
# end main
```

