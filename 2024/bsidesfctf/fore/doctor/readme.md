---
CTF: BSidesSF'24
Category: difor
Points: "100"
Date: 2024-05-04
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
CTF{st0ck_cut3_p1c5}
```

### Details

Description

> This doc seems to be hiding something. Can you find what's hidden?
> 
> Flag is in the form CTF{-----_----_----}.
> Author: ansh 

Files
- SuperSecretWordDoc.docx


![](assets/Pasted%20image%2020240504183221.png)

Using `binwalk` we can find some images that were in the file
![](assets/Pasted%20image%2020240504183750.png)

Opening `image0.png` we get the flag

![](assets/Pasted%20image%2020240504183820.png)

```
CTF{st0ck_cut3_p1c5}
```

Full image:

![](source/image0.png)