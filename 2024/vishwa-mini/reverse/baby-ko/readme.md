---
CTF: VishwaCTF 2024 24h
Name: Baby ko base Pasand hai
Category: reverse
Points: 100
Date: 2024-01-04
Solved?: true
---
----
[<- Home](../../)
### TL;DR

Base32 string in .exe file

**Flag**

```
VishwaCTF{ky4_b4by_k0_s4ch_m3in_BASE_p4s4nd_h41??}
```


### Details

```bash
$ strings exe
```

![](assets/1.png)

got this string
```
KZUXG2DXMFBVIRT3NN4TIX3CGRRHSX3LGBPXGNDDNBPW2M3JNZPUEQKTIVPXANDTGRXGIX3IGQYT6P35
```

via cyberfchef decoding 

![](assets/2.png)

![](assets/3.png)
