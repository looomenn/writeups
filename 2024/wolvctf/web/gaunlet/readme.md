---
CTF: WolvCTF'24
Category: web
Points: "100"
Date: 2024-03-16
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
wctf{w3_h0p3_y0u_l34rn3d_s0m3th1ng_4nd_th4t_w3b_c4n_b3_fun_853643}
```

### Details

Description

> Can you survive the gauntlet?
> 
> 10 mini web challenges are all that stand between you and the flag.
> 

Files
- app.py


solve for `/hidden83365193635473293` (page 9 out of 10)

```python
#!/usr/bin/env python3

import requests as rq
from tqdm import tqdm

URL: str = 'https://gauntlet-okntin33tq-ul.a.run.app/hidden83365193635473293'

def main():

    session = rq.Session()

    for i in tqdm(range(1000)):
        req = session.get(URL)
        print(session.cookies)

        print(f'Req number {i}', end='\r')

    print(response.text)
    print(session.cookies.get_dict())

if __name__ == "__main__":
    main()

```
