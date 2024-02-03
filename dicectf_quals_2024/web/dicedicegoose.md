---
CTF: Dice CTF 2024 Quals
"Challenge name:": Dice Dice Goose
"Challenge category:": We
"Challenge point:": 109
Date: 2024-02-03
Solved?: true
---
----
### TL;DR

To get a unique part of the flag, you need to get a specific history of moves

![[Pasted image 20240203160345.png]]

**Flag**

```
dice{pr0_duck_gam3r_AAEJCQEBCQgCAQkHAwEJBgQBCQUFAQkEBgEJAwcBCQIIAQkB}
```


### Details

We got this noice looking web DDG. 

![[Pasted image 20240203160212.png]]

Using browser utilities, check the file structure of the website

![[Pasted image 20240203160635.png]]

Here we can see script tag that, actualy, controls all actions on the page. Let's dive into.



---
### Appendix

solve.py
```python
function encode(history) {
    const data = new Uint8Array(history.length * 4);
    
    let idx = 0;
    for (const part of history) {
      data[idx++] = part[0][0];
      data[idx++] = part[0][1];
      data[idx++] = part[1][0];
      data[idx++] = part[1][1];
    }
    
    let prev = String.fromCharCode.apply(null, data);
    let ret = btoa(prev);
    return ret;
}
  
const history = [
	[
	  [0, 1],
	  [9, 9],
	],
	[
	  [1, 1],
	  [9, 8],
	],
	[
	  [2, 1],
	  [9, 7],
	],
	[
	  [3, 1],
	  [9, 6],
	],
	[
	  [4, 1],
	  [9, 5],
	],
	[
	  [5, 1],
	  [9, 4],
	],
	[
	  [6, 1],
	  [9, 3],
	],
	[
	  [7, 1],
	  [9, 2],
	],
	[
	  [8, 1],
	  [9, 1],
	],
];
  
const encodedResult = encode(history);
console.log("Encoded:", encodedResult);

# Result :: Encoded: AAEJCQEBCQgCAQkHAwEJBgQBCQUFAQkEBgEJAwcBCQIIAQkB
```
