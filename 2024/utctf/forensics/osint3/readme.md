---
CTF: UTCTF'24
Category: difor
Points: 892
Date: 2024-03-30
Solved?: true
---
----
[<- Home](../../)
### TL;DR

IP in the Fadom logs

**Flag**

```
181.41.206.31
```

### Details

Description

> Can you find the person's IP address? **Flag format is XXX.XXX.XXX.XXX**
> By mzone (@mzone on discord)

Hint 1
If you wound up on another (unrelated) discord server, then one of the sites you visited is too new.

Hint 2
All in scope accounts follow the same naming convention. Once you've reached a centralized location any sites you need can be reached in at most 3 clicks.

Files
< nope :/ >


We can find reddit from his linktree - https://linktr.ee/coleminerton

![](assets/Pasted%20image%2020240330222218.png)


In the first post, we can see that `Cole Minerton` is a new mod in subreddit 'r/tinyislandsurvival' 

![](assets/Pasted%20image%2020240330222446.png)

Than, in the description of the subreddit we can find discord server, but as it states in **Hint 1** it's unrelated

![](assets/Pasted%20image%2020240330222744.png)

Apparently, reddit is `to new`  but not wrong one! So, going to subdomain `old` gives us the Fandom Wiki page - https://tiny-island-survival.fandom.com/wiki/**Tiny_Island_Survival_Wiki**

![](assets/Pasted%20image%2020240330222919.png)
Link - https://old.reddit.com/r/tinyislandsurvival/


Where admin is our person
![](assets/Pasted%20image%2020240330222954.png)

After looooong seassion of searching in the logs, all we needed to do is: 

1. On home page, go to history page.
![](assets/Pasted%20image%2020240330223106.png)

2. Finding our target IP in logs. 
![](assets/Pasted%20image%2020240330223203.png)


Flag:
```
181.41.206.31
```