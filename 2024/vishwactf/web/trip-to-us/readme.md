---
CTF: VishwaCTF2024
Category: web
Points: 
Date: 
Solved?:
---
----
### TL;DR

**Flag**

```
VishwaCTF{y0u_g0t_th3_7r1p_t0_u5}
```


### Details

Description
```
IIT kharakpur is organizing a US Industrial Visit. The cost of the registration is $1000. But as always there is an opportunity for intelligent minds. Find the hidden login and Get the flag to get yourself a free US trip ticket.
```


![](img-1.png)

![](img-2.png)

![](img-3.png)

And use basic sql injection for login bypass (username: admin, password: `' or '1'='1`)

![](assets/flag.png)