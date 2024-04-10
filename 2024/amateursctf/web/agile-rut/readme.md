---
CTF: AmateursCTF'24
Category: web
Points: "173"
Date: 2024-04-10
Solved?: false
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
amateursctf{0k_but_1_dont_like_the_jbmon0_===}
```

### Details

Description

> check out this cool font i made!
> http://agile-rut.amt.rs
> hint: if you get something that looks like the flag try pasting it into the box.

This chall was cursed... Here you can see all my tries for the flag

```
BANGlig.a.m.a.t.e.u.r.s.C.T.F.braceleft.zero.k.underscore.b.u.t.underscore.one.underscore.d.o.n.t.underscore.l.i.k.e.underscore.t.h.e.underscore.j.b.m.o.n.zero.underscore.equal.equal.equal.bracerightlig.f.f.ilig.f.f.llig.f.flig.f.ilig.f.l
```

```
amateursCTF{0k_but_1_dont_like_the_jbmon0_===}
```

```
amateursctf{zerok_but_one_dont_like_the_jbmonzero_===}
```


```
amateursCTF{zerok_but_one_dont_like_the_jbmonzero_===}
```

```
a.m.a.t.e.u.r.s.C.T.F.braceleft.zero.k.underscore.b.u.t.underscore.one.underscore.d.o.n.t.underscore.l.i.k.e.underscore.t.h.e.underscore.j.b.m.o.n.zero.underscore.equal.equal.equal.braceright
```

```
lig.a.m.a.t.e.u.r.s.C.T.F.braceleft.zero.k.underscore.b.u.t.underscore.one.underscore.d.o.n.t.underscore.l.i.k.e.underscore.t.h.e.underscore.j.b.m.o.n.zero.underscore.equal.equal.equal.braceright
```

Orignaly, I found it using [FontDrop](https://fontdrop.info. There was a possibility to see the flag on the glyphs page in the name of that glyph

![](assets/Pasted%20image%2020240410181725.png)

But... it was a bait (or not lol). Using [GlyphStudio](https://www.glyphrstudio.com/app/) we can see (excat same file) the flag in the name of that glyph

![](assets/Pasted%20image%2020240410181842.png)

```
Ligature amateursctf{0k_but_1_dont_like_the_jbmon0_===}
```

SO, ALL THAT TIME IT WAS `ctf`  NOT `CTF`.. 

![](assets/Pasted%20image%2020240410182027.png)