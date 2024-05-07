---
CTF: spaceheroes'24
Category: difor
Points: "100"
Date: 2024-04-13
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
shctf{s0_l0ng_4nd_th4nks_f0r_4ll_th3_flags}
```

### Details

Description

> Petey the Panther has stumbled upon the greatest treasure this side of the Milky Way: a bonafide Hitchhikers Guide to the Galaxy! What kind of secrets does this thing hold?
> 
> Author: Zero

Files
- A Real Hero.jpeg
![](source/A_Real_Space_Hero.jpg)

Using `binwalk` we can find seeeeeeeeeeeecrets

![](assets/Pasted%20image%2020240413141852.png)

Using figma, assembling the pieces together

![](assets/Figma_MLzjEGp1dN.gif)

Scanning it, we get the flag

```
shctf{s0_l0ng_4nd_th4nks_f0r_4ll_th3_flags}
```