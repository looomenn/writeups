---
CTF: VishwaCTF2024
Category: crypto
Points: 200
Date: 2024-03-04
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
VishwaCTF{h3ad3r5_f0r_w1nn3r5}
```

### Details

Description

> My girlfriend and I captured our best moments of Valentine's Day in a portable graphics network. But unfortunately, I am not able to open it as I accidentally ended up encrypting it. Can you help me get my memories back?
> 
> **Author : Pushkar Deore**

Files

![](assets/files.png)

We have two files, a python file and an encrypted png file

```python
from PIL import Image
from itertools import cycle

def xor(a, b):
    return [i^j for i, j in zip(a, cycle(b))]

f = open("original.png", "rb").read()
key = [f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7]]

enc = bytearray(xor(f,key))

open('enc.txt', 'wb').write(enc)

```

Here is the catch. The key is a list of the first 8 bytes of png image. So, it is static. 

All we need, is to xor our `enc.txt` with new key

```
key = [137, 80, 78, 71, 13, 10, 26, 10]
```

solve.py

```python
from PIL import Image
from itertools import cycle
import io

def xor(a, b):
    return [i^j for i, j in zip(a, cycle(b))]

f = open("enc.txt", "rb").read()

key = [137, 80, 78, 71, 13, 10, 26, 10]

dec = bytearray(xor(f, key))

image = Image.open(io.BytesIO(dec))
image.show()
```

After running it, we got image with our flag

![](assets/flag.png)
