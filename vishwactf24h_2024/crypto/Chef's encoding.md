---
CTF: VishwaCTF 2024 24h
"Challenge name:": Chef's Encoding Message
"Challenge category:": crypto
"Challenge point:": 100
Date: 2024-01-04
Solved?:
---
----
### TL;DR

input :
```
sxu3o_e05v3_xmbigk01_m4ztoi0g1ns!5
```

**Flag**
```
VishwaCTF{ch3f_l0ve5_3ncrypt10n_a4lg0r1thm5!}
```

### Details

https://discuss.codechef.com/t/encoded-meassage/19469

> Chef has a message, which is a string S with length N containing only lowercase English letters. It should be encoded in two steps as follows:
> 
> Swap the first and second character of the string S, then swap the 3rd and 4th character, then the 5th and 6th character and so on. If the length of S is odd, the last character should not be swapped with any other.  
> Replace each occurrence of the letter ‘a’ in the message obtained after the first step by the letter ‘z’, each occurrence of ‘b’ by ‘y’, each occurrence of ‘c’ by ‘x’, etc, and each occurrence of ‘z’ in the message obtained after the first step by ‘a’.

Throw to some AI (worked only in Google Bard) prompt like that:

```
given input 

sxu3o_e05v3_xmbigk01_m4ztoi0g1ns!5


hint: 
Chef has a message, which is a string S with length N containing only lowercase English letters. It should be encoded in two steps as follows:
Swap the first and second character of the string S, then swap the 3rd and 4th character, then the 5th and 6th character and so on. If the length of S is odd, the last character should not be swapped with any other.
Replace each occurrence of the letter ‘a’ in the message obtained after the first step by the letter ‘z’, each occurrence of ‘b’ by ‘y’, each occurrence of ‘c’ by ‘x’, etc, and each occurrence of ‘z’ in the message obtained after the first step by ‘a’.
```

and vu a la 

![[Pasted image 20240204131244.png]]

---
### Appendix

encoder.py
```python
def encode_message(message):
    """ Chef code encoding """
    
    swapped_message = ''.join([message[i + 1] + message[i] if i + 1 < len(message) else message[i] for i in range(0, len(message), 2)])
    encoded_message = ''.join([chr(ord('z') - (ord(char) - ord('a'))) if char.isalpha() else char for char in swapped_message])

    return encoded_message

original_message = "sxu3o_e05v3_xmbigk01_m4ztoi0g1ns!5"
encoded_result = encode_message(original_message)
print(encoded_result) # ch3f_l0ve5_3ncrypt10n_a4lg0r1thm5!

```
