---
CTF: AmateursCTF'24
Category: misc
Points: "256"
Date: 2024-04-06
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
amateursCTF{inverse_transformations}
```

### Details

Description

> You can make anything sound like laughing if you try hard enough with an imagination. mussmile
> 

Files
laughing.wav

So, we get the `.wav` file with high pitched "laugh". 

![](assets/Pasted%20image%2020240406213233.png)

From the audio pattern we can clearly see it's was reversed

![](assets/Pasted%20image%2020240406213258.png)

Using special tools, reversing the audio 

![](assets/Pasted%20image%2020240406213328.png)


So, now we need to lower down the pitch to actually hear something

Using `Change Speed and Pitch` lowering down it to ~ `0.100`. At this speed multiplier we can start hearing some lorem ipsum 

![](assets/Pasted%20image%2020240406213538.png)

And after some listetining we can hear the flag at this part

![](assets/Pasted%20image%2020240406214115.png)

```
Thank you for being so persistent. Your flag is inverse transformations. Put an underscore in between two words and wrap it into the flag wrapper. 
```