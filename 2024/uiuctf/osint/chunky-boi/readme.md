---
CTF: uiuctf'24
Category: osint
Points: 319
Date: 2024-06-30
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
uiuctf{Boeing C-17 Globemaster III, 47.462, -122.303}
```

### Details

**Description:**
Now that's a BIG plane! I wonder where it is. Flag format: uiuctf{plane type, coordinates of the aircraft} Example: uiuctf{Airbus A380-800, 40.036, -88.264}
For coordinates, just omit the digits, do not round up. Precision is the same as the one in the example. The aircraft name is the same as Wikipedia page title. You can extract enough information from this image to answer this. You DO NOT need to register any accounts, all the information is public.
Flag format clarification: The last digit of the first coordinate is even, and the last digit of the second coordinate is odd.


**Files:**

![](source/chal.jpg)


Now we know it's `Alaska Airlines`

![](assets/Pasted%20image%2020240630222056.png)

Using jetphotos.com we can find that plane ID

![](assets/Pasted%20image%2020240630224317.png)

So it's  `Boeing C-17A Globemaster III`, `P-182`, `07-7182`

Here are two ways to find the correct spot

**No. 1 - Transportation company**

![](assets/Pasted%20image%2020240630235853.png)

By the building pattern via google lens find that it is https://www.transiplex.com

From their site, track to the Sea-Tac airport

![](assets/Pasted%20image%2020240701000732.png)

Proof 

![](assets/prof1.png)

So the cameramen's view should probably be like this...

![](assets/prof2.png)


**No. 2 - C-17 flight history**

1. check photo exif info, and find out that it was created `2024:05:11 16:44:28.107`

![](assets/Pasted%20image%2020240701001832.png)

2. using https://globe.adsbexchange.com/ check that date for `07-7182`

![](assets/Pasted%20image%2020240701001940.png)

find out out C-17 was in Seattle on that day


So, it's `Boeing C-17 Globemaster III` and it is parked +- here `47.462, -122.303`


