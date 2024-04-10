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
challenge.png
main.py
and ip for nc server 

![](source/challenge.png)


By flags in the left corner of the image, we can pin point that is near the `Washington Monument` in DC

Running around in the street view, we can find cherry bloom with specific branch pattern

![](assets/geolocation.png)
GEO: `~ 38.889107, -77.033531`

After pasting these coordinates to the nc server we get the flag!

```
amateursCTF{l00k1ng_l0v3ly_1n_4k}
```

![](assets/Pasted%20image%2020240406091104.png)