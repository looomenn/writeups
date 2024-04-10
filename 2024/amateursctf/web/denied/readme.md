---
CTF: AmateursCTF'24
Category: web
Points: 53
Date: 2024-04-05
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
amateursCTF{s0_m@ny_0ptions...}
```

### Details

Description

> what options do i have?
> http://denied.amt.rs
> 

Files
- index.js

```js
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  if (req.method == "GET") return res.send("Bad!");
  res.cookie('flag', process.env.FLAG ?? "flag{fake_flag}")
  res.send('Winner!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

```


Using burp suite change the request method to `HEAD` 
 fromAnd the response we get the url-encoded flag

![](assets/Pasted%20image%2020240405205203.png)

```
amateursCTF{s0_m@ny_0ptions...}
```

