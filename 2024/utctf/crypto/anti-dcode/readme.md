---
CTF: UTCTF'24
Category: crypto
Points: 100
Date: 2024-03-31
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
43flag{rip_dcode}
```

### Details

Description

> I've heard that everyone just uses dcode.fr to solve all of their crypto problems. Shameful, really.
> 
> This is really just a basic Caesar cipher, with a _few_ extra random characters on either side of the flag. Dcode can handle that, right? >:)
> 
> The '{', '}', and '_' characters aren't part of the Caesar cipher, just a-z. As a reminder, all flags start with "utflag{".
> 
> By Khael (Malfuncti0nal on Discord).


Files
LoooongCaesarCipher.txt

By selecting different values of the ciphers, we will reach 8 -- that's our shift

![](assets/Pasted%20image%2020240331024656.png)

![](assets/Pasted%20image%2020240331024913.png)

Finding that one part in the file

![](assets/Pasted%20image%2020240331024858.png)

And converting full string enclosed with `{}` brackets 

```
cbntio{zqx_lkwlm}
```

![](assets/Pasted%20image%2020240331025030.png)

Flag: 
```
utflag{rip_dcode}
```

