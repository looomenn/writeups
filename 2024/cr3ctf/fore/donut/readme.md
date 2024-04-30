---
CTF: cr3ctf'24
Category: forensics
Points: 93
Date: 2024-04-27
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
cr3{w3_4r3_411_10v3_d0n7T5!1}
```

### Details

Description

> Do you want some donuts? I have one for you :)
> 
> author: dxq

Files
- for_donut.7z


Formatted `donut.py`

```python
import math
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_frame(A, B):
    screen = [' '] * 1760
    z_buffer = [0] * 1760
    for j in range(0, 628, 7):  # j goes from 0 to 2*pi in steps
        for i in range(0, 628, 2):  # i goes from 0 to 2*pi in smaller steps
            # Precompute sine and cosine values
            sin_i = math.sin(i / 100)
            cos_j = math.cos(j / 100)
            sin_A = math.sin(A)
            cos_A = math.cos(A)
            sin_B = math.sin(B)
            cos_B = math.cos(B)

            # Calculate 3D coordinates after rotation
            circle_x = sin_i
            circle_y = cos_j + 2
            scale = 1 / (circle_x * circle_y * sin_A + cos_A + 5)
            x = int(40 + 30 * scale * (circle_y * cos_A - sin_i * cos_j * sin_A))
            y = int(12 + 15 * scale * (circle_y * sin_A + sin_i * cos_j * cos_A))

            # Calculate brightness index
            L = sin_i * cos_j * sin_B - cos_A * cos_j * sin_i - sin_A * sin_j + cos_B * cos_j * circle_x
            if L > 0:
                brightness_index = int(8 * L)
                if 0 <= x < 80 and 0 < y < 22:
                    # Compare depth and update screen if closer
                    flat_index = y * 80 + x
                    if scale > z_buffer[flat_index]:
                        z_buffer[flat_index] = scale
                        screen[flat_index] = ".,-~:;=!*#$@"[brightness_index if brightness_index < 12 else 11]
    return ''.join(screen)

def main():
    A = B = 0
    while True:
        clear_screen()
        frame = calculate_frame(A, B)
        print("\x1b[H", end='')  # Move cursor to top-left
        for i in range(0, 1760, 80):  # Print the frame
            print(frame[i:i+80])
        A += 0.04  # Increment angles for rotation
        B += 0.02

if __name__ == "__main__":
    main()

```

This code prints and spins 3d donut in the console. My first thought was that it was just a rabbit hole. (update: yes it was)

using `7z l for_donut.7z` we can see that there is a `.git` folder. 

![](assets/Pasted%20image%2020240427172318.png)


Using `git status` we can see that there is some error in the `index` file

![](assets/Pasted%20image%2020240427204415.png)

Some kind of tree and fake flag

![](assets/Pasted%20image%2020240427204617.png)

So, because of it, we can't use commands like `git log`. That it, we need to investigate files manually. 

From the `HEAD` file we can find the current history

```
e1cf8e13bfe7f2b9522642a878368677621349b1 e1cf8e13bfe7f2b9522642a878368677621349b1 dxqwww <minikkat1337@gmail.com> 1713541575 +0300	checkout: moving from master to flag
e1cf8e13bfe7f2b9522642a878368677621349b1 2a461812df0b80851da28cf6e69f3a2d84129b01 dxqwww <minikkat1337@gmail.com> 1713541687 +0300	commit: added flag
2a461812df0b80851da28cf6e69f3a2d84129b01 e1cf8e13bfe7f2b9522642a878368677621349b1 dxqwww <minikkat1337@gmail.com> 1713541710 +0300	checkout: moving from flag to master

```

Using the command `git cat-file -p <filename>` (read more about this cmd [here](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)) for every hash we can find one associated with a flag. 

```
git cat-file -p 2a461812df0b80851da28cf6e69f3a2d84129b01
```

![](assets/Pasted%20image%2020240427205058.png)

From it, we get a tree hash with a flag file in it. 

![](assets/Pasted%20image%2020240427205137.png)

```
git cat-file -p 3e99af25da2bfd1afa8adf7e576f059d25e97dd0
```

Using the same command on the flag hash we get the flag

```
git cat-file -p 18647d6429b7814c03fb3cf1015adbd73c4ab23f
```

![](assets/Pasted%20image%2020240427205256.png)

flag:
```
cr3{w3_4r3_411_10v3_d0n7T5!1}
```

