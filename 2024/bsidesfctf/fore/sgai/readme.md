---
CTF: BSidesSF'24
Category: difor
Points: "100"
Date: 2024-05-04
Solved?:
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
ctf{fake_flag}
```

### Details

Description

> This image from the past may hold the key to our future survival if you can find the hidden flag! (This is flag 1 of 4)
> 
> Author: symmetric


Files
- sgai.tar.xz


From the `notes.txt` in that archive

```
This is 4 challenges in one file! That is, there are 4 flags,
coresponding to:

sgai-1
sgai-2
sgai-3
sgai-4

If you find a flag and it doesn't work against one of these you'll
need to try it in the others. There are no 'decoy' flags so if you
find a flag it definitely is correct for one of them.
```

From the strings we get the first (`sgai-1`) flag 

![](assets/Pasted%20image%2020240504184632.png)

```
CTF{i_name_thee_flag}
```

From the image itself we get the flag for the `sgai-3` 

![](assets/Pasted%20image%2020240504185420.png)

```
CTF{invisibility_cloak}
```
