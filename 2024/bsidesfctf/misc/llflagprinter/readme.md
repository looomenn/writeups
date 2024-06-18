---
CTF: BSidesSF'24
Category: misc
Points: "100"
Date: 2024-05-05
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
CTF{llvm_a_llm_for_v_enthusiasts}
```

### Details

Description

> We've gotten the LLVM compilation started for you, now you just need to complete it for your system.
> 
> Author: symmetric
> 


Files
- llflagprinter.bc

We can directly execute the LLVM bitcode using `lli` cmd and obtain the flag.

![](assets/Pasted%20image%2020240505210314.png)

```
CTF{llvm_a_llm_for_v_enthusiasts}
```

