---
CTF: UTCTF'24
Category: difor
Points: 100
Date: 2024-03-30
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
utflag{s1mple_w1z4rding_mist4k3s}
```

### Details

Description

> Magical contracts are hard. Occasionally, you sign with the flag instead of your name. It happens.
> 
> By Samintell (@samintell on discord)

Files
Contract.pdf


![](assets/Pasted%20image%2020240330131341.png)

Checking with binwalk. File indeed has some files in it.

![](assets/Pasted%20image%2020240330131406.png)

https://tools.pdf24.org/en/extract-images

Using some random image extractor-from-pdf tool we can get the flag

![](assets/Pasted%20image%2020240330230816.png)