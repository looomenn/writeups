---
CTF: spaceheroes'24
Category: difor
Points: "-1"
Date: 2024-04-13
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
shctf{1_sh0uld_try_h1d1ng_1n_th3_ch3cksum_n3xt_t1me_0817}
```

### Details

Description

> I think aliens are testing us again and they they are poking fun at our internet protocols by using them in close proximity to earth. We were able to intercept something but I cant figure out what it is. Take a crack at it for me.
> 
> Author: Josh

Files
- space.pcapng

Flag was encoded in the `window` size field in the TCP packets

![](assets/Pasted%20image%2020240413145453.png)
![](assets/Pasted%20image%2020240413145526.png)
Setting `tcp.window_size > 0` make it easier to combine them. 


From it we get the flag

```
shctf{1_sh0uld_try_h1d1ng_1n_th3_ch3cksum_n3xt_t1me_0817}
```