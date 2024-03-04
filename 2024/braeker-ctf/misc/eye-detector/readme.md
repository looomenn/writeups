---
CTF: Braeker CTF
Category: misc
Points: 
Date: 2024-02-23
Solved?:
---
----
### TL;DR

Flag is revealed after reversing linear blur effect via [opencv](https://github.com/opencv/opencv/blob/3.2.0/samples/python/deconvolution.py)

**Flag**

```
brck{4ppr04ch1tfr0M4D1ff3r3ntAngl3}
```


### Details

![[Pasted image 20240224203836.png]]

Description
```
A creaky old bot is zooming in and out of an eye chart. "Can you read the bottom line?" the doctor asks. "No way, " the bot replies. "At a certain distance my view becomes convoluted. Here, I'll make a screenshot."

You and the doctor look at the screenshot. Can you tell what's wrong with the bot's visual processor?
```

Files needed from cv2 lib
![[Pasted image 20240224204354.png]]


