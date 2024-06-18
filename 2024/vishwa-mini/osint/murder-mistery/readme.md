---
CTF: VishwaCTF 2024 24h
"Challenge name:": Murder Mistery
"Challenge category:": osint
"Challenge point:": 100
Date: 2024-01-04
Solved?:
---
----
### TL;DR

**Flag**

```
VishwaCTF{evil_shadow}
```


### Details

IMb postal code

```
ATTTFTADAFFTDTTAADTDTTATDAFDDDATATDDDDTADFAFADFATATFDFADDFFAFATDT
```

https://postalpro.usps.com/ppro-tools/encoder-decoder

![[assets/1.png]]
Combine all numbers in one strings

```
101 118 105 108 95 115 104 97 100 111 119
```

and convert in to ascii:
```
evil_shadow
```



