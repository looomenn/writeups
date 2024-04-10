---
CTF: AmateursCTF'24
Category: osint
Points: "353"
Date: 2024-04-06
Solved?:
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
amateursCTF{s1gn1ng_a1nt_g0nna_st0p_0ur_brut3}
```

### Details

Description

> hopefully redacted enough, im kind of bad at this whole iphone photography thing so it took a few attempts to make this intentionally cringe msfrog in front of the flag, hopefully no one can guess the flag using this info


Files 
- IMG_7276.jpg

![](source/IMG_7276.jpg)

It's turned out to be MUCH easier than I expected. From the given image, we can see, that the image with the flag is located in some discord channel but we don't know its name. 

But, from the chall description we have a hint: 

> photography thing so it took a **few attempts** to make this intentionally cringe msfrog
> 

So, all we need to do is just guess the correct number for the file name `IMG_72{}.jpg` by pasting the full link in any discord chat. 

![](assets/Pasted%20image%2020240410175031.png)

And on `7262` we find the flag lol

Link: https://cdn.discordapp.xyz/attachments/1098086661847535719/1226012804150984754/IMG_7262.jpg

```
amateursCTF{s1gn1ng_a1nt_g0nna_st0p_0ur_brut3}
```

![](https://cdn.discordapp.xyz/attachments/1098086661847535719/1226012804150984754/IMG_7262.jpg)
