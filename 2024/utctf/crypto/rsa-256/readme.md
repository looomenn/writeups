---
CTF: UTCTF'24
Category: crypto
Points: 100
Date: 2024-03-30
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
utflag{just_send_plaintext}
```

### Details

Description

> Based on the military-grade encryption offered by AES-256, RSA-256 will usher in a new era of cutting-edge security... or at least, better security than RSA-128.
> 
> By Jeriah (@jyu on discord)


Files
vals.txt


Given file with next content
```
N = 77483692467084448965814418730866278616923517800664484047176015901835675610073
e = 65537
c = 43711206624343807006656378470987868686365943634542525258065694164173101323321
```

Just use https://www.dcode.fr/rsa-cipher 
![](assets/Pasted%20image%2020240330223558.png)