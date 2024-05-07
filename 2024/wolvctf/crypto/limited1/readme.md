---
CTF: WolvCTF'24
Category: crypto
Points: "100"
Date: 2024-03-18
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
wctf{f34R_0f_m1ss1ng_0ut}
```

### Details

Description

>It's pretty easy to find random integers if you know the seed, but what if every second has a different seed?


Files
- chall.py

solve.py

```python
#!/usr/bin/env python3

import time
import random

correct = [189, 24, 103, 164, 36, 233, 227, 172, 244, 213, 61, 62, 84, 124, 242, 100, 22, 94, 108, 230, 24, 190, 23, 228, 24]

def solve():
    for time_cycle in range(int(time.time()) % 256 - 1000, int(time.time()) % 256 + 100):
        flag = []
        print(time_cycle, end='\r')

        for i, correct_value in enumerate(correct):
            random.seed(i + time_cycle)
            flag_byte = correct_value ^ random.getrandbits(8)
            flag.append(flag_byte)

        if all(byte >= 32 and byte <= 126 for byte in flag):
            print(f'Seed: {time_cycle}')
            return bytes(flag).decode('utf-8')
    
    return "Could not decode the flag."


if __name__ == "__main__":
    print(solve())
# end main
```

