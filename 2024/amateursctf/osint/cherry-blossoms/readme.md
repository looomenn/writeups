---
CTF: AmateursCTF'24
Category: osint
Points: 195
Date: 2024-04-06
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
amateursCTF{l00k1ng_l0v3ly_1n_4k}
```

### Details

Description

> average southern californian reacts to DC weather. amazing scenery though at the time.
> 
> Find the coords of this image!

Files
- challenge.png
- main.py
- ip for nc server 

![](source/challenge.png)


By the flags in the left corner of the image, we can pinpoint that it is near the `Washington Monument` in DC

Running around using Google Street View, we can find the cherry blossom with a specific branch pattern

![](assets/geolocation.png)

GEO: `~ 38.889107, -77.033531`

And from the nc we get the flag 

```
amateursCTF{l00k1ng_l0v3ly_1n_4k}
```

![](assets/Pasted%20image%2020240406091104.png)