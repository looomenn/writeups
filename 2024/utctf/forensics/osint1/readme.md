---
CTF: UTCTF'24
Category: difor
Points: 580
Date: 2024-03-30
Solved?: true
---
----
[<- Home](../../)
### TL;DR

Flag was in the `.pdf` (leaked contract) in the discord server (has never happened before, of course lol )

**Flag**

```
utflag{discord_is_my_favorite_document_leaking_service}
```

### Details

Description

> It seems like companies have document leaks all the time nowadays. I wonder if this company has any.
> (NOTE: It turns out there's also an actual company named Kakuu in Japan. The real company is not in scope. Please don't try and hack them.)
> By mzone (@mzone on discord)
>

Files
< nope :/ >

We get some fake corp website - `Kakuu Corp`

![](assets/Pasted%20image%2020240330201433.png)

By searching every team member's name in google, we can find `Cole Minerton`'s youtube account

![](assets/Pasted%20image%2020240330200601.png)
Link - https://www.youtube.com/@ColeMinerton

We can see some discord from it  - https://discord.gg/re9ez8ey

From it, in the general chat, we can find some `.pdf` file

![](assets/Pasted%20image%2020240330200849.png)

And... in it we can find the flag

![](assets/Pasted%20image%2020240330201245.png)

Flag:
```
utflag{discord_is_my_favorite_document_leaking_service}
```


Added this pdf to source folder :> ([VT](https://www.virustotal.com/gui/file/7ec1c6c1cbac009d623fae192322a86d9adf058330f1b77ab979ef973021918c))

![](assets/Pasted%20image%2020240330201710.png)
