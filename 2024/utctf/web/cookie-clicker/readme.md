---
CTF: UTCTF'24
Category: web
Points: 100
Date: 2024-03-31
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
utflag{y0u_cl1ck_pr3tty_f4st}
```

### Details

Description

> I tried to make my own version of cookie clicker, without all of the extra fluff. Can you beat my highscore? 
> 
> 
> By Khael (@malfuncti0nal on discord)
>

Files
< nope :/ >

Solve for browser console

```js
// Find the image element by its ID
var imageElement = document.getElementById('cookieImage');

// Check if the image element exists
if (imageElement) {
    // Simulate 11 million clicks
    var numberOfClicks = 11000000;
    for (var i = 0; i < numberOfClicks; i++) {
        // Create and dispatch a click event on the image element
        var clickEvent = new MouseEvent('click', {
            view: window,
            bubbles: true,
            cancelable: true
        });
        imageElement.dispatchEvent(clickEvent);
    }
} else {
    console.error('Image element with ID "cookieImage" not found.');
}
```

