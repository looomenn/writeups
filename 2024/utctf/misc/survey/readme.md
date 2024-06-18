---
CTF: UTCTF'24
Category: misc
Points: 100
Date: 2024-03-31
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
utflag{byethanks}
```

### Details

Why answer the form when you can see answers in the source code :>

```
var FB_PUBLIC_LOAD_DATA_ = [

...

, [null, "Any other feedback?"]]], ["thank yoU for filling ouT our Feedback form!  pLeAse rate the ctf on ctftime when you Get a chance. rememBer that we will accept Your writEups for forTy-eigHt hours After the competitioN for writeup prizes. hooK em hornS!", 0, 0, 0, 0]

...

]
```

```
UTFLAG{BYETHANKS}
```
