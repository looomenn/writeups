---
CTF: VishwaCTF2024
Category: web
Points: 200
Date: 2024-03-03
Solved?: true
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
IIT kharakpur is organizing a US Industrial Visit. The cost of the registration is $1000.
But as always there is an opportunity for intelligent minds. Find the hidden login and Get the flag to get yourself a free US trip ticket.
```


![](assets/img-1.png)

Changing `User-Agent` to `IITIAN`

![](assets/img-2.png) 

After that, we get the login page. User login can be found in `alt` of the background image

![](assets/img-3.png)

Fro the password, we can you basic `sql injection` for login bypass (username: admin, password: `' or '1'='1`)

![](assets/flag.png)
