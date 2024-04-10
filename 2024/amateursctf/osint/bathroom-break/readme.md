---
CTF: AmateursCTF'24
Category: osint
Points: 476
Date: 2024-04-06
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
amateursCTF{jk_i_lied_whats_a_bathroom_0f9e8d7c6b5a4321}
```

### Details

Description

> I was on an in-state skiing trip with my family when we decided to go out and see some sights. I remember needing to go to the bathroom near where these pictures were taken and then leaving a review. Can you find this review for me?


Files
- 2 images

![](source/67BC754A-C818-4358-8E4F-16DF8B2230E8.jpg)

![](source/493B0E69-C226-4171-B565-2E68ECF25A29.jpg)


From the first image, using goole lens, we can find that it's `HOT CREEK GEOLOGICAL SITE `

![](assets/Pasted%20image%2020240406083016.png)


And conformation of that
GEO: `37.661039, -118.828682`

![](assets/geolocation_01.png)

That said, we need to find some bathroom review near this place.

Near it, there are `Vault Toiltes`

![](assets/Pasted%20image%2020240406084344.png)

And... there is a *fishy* review

![](assets/Pasted%20image%2020240406084412.png)

Using [WhereItGoes](https://wheregoes.com/trace/20241848939/) checking were it goes lol. As it turns out, it redirects to pastebin 

![](assets/Pasted%20image%2020240406084513.png)

 https://pastebin.com/jxaznYqH

The flag is located at the bottom end of the story about Flagotopia

![](assets/Pasted%20image%2020240406084731.png)

```
amateursCTF{jk_i_lied_whats_a_bathroom_0f9e8d7c6b5a4321}
```