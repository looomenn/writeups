---
CTF: WolvCTF'24
Category: difor
Points: "398"
Date: 2024-03-17
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
wctf{l3tS_3teRn4lLy_g0_bLU3_7n9wm4iWnL}
```

### Details

Description

> Hi I recently had my passwords and other sensitive data leaked, but I have no idea how. Can you figure out how the attacker got in to my PC?


Files
- network-capture.pcap

*I'm writing this writeup more than 2 months after the completion of the CTF. There are no original screenshots, so I'll take it from the official [WU](https://github.com/WolvSec/WolvCTF-2024-Challenges-Public/blob/master/forens/eternally-pwned/Infiltration/solution/solve.md).* 


Notice something is up with the SMB traffic, possibly by indicators of compromise

![](assets/Pasted%20image%2020240507142226.png)

You can see some base64 strings in the payload. So we need to find the flag in echo request and Trans2 Secondary Request, both part of MS17-10 payload ( MS17-10 EternalBlue attack )

![](assets/Pasted%20image%2020240507142331.png)

![](assets/Pasted%20image%2020240507142336.png)

All strings combined: 


```
d2N0ZntsM3RTXw==

M3RlUm40bEx5X2cwXw==

YkxVM183bjl3bTRpV25MfQ==
```

gives as the flag

```
wctf{l3tS_3teRn4lLy_g0_bLU3_7n9wm4iWnL}
```