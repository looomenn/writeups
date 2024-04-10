---
CTF: AmateursCTF'24
Category: crypto
Points: "247"
Date: 2024-01-09
Solved?:
---
----
[<- Home](../../)
### TL;DR

**Original code author** - [N1k4](https://discord.com/channels/1098085484896469012/1098293803292569651/1227454779299463239) 

**Flag**

```
amateursCTF{here's_the_flag_you_requested.}
```

### Details

Description

> I need help factoring this modulus, it looks suspicious, but I can't factor using any conventional methods.
> 


Files
- output.txt
- unsuspicious-rsa.py

solve.py
```python
#!/usr/bin/env python3

from Crypto.Util.number import *
from z3 import *

N = 172391551927761576067659307357620721422739678820495774305873584621252712399496576196263035396006999836369799931266873378023097609967946749267124740589901094349829053978388042817025552765214268699484300142561454883219890142913389461801693414623922253012031301348707811702687094437054617108593289186399175149061
E = 65537
C = 128185847052386409377183184214572579042527531775256727031562496105460578259228314918798269412725873626743107842431605023962700973103340370786679287012472752872015208333991822872782385473020628386447897357839507808287989016150724816091476582807745318701830009449343823207792128099226593723498556813015444306241


def factorial(n):
    if n == 0: return 1
    return factorial(n-1) * n


def solve(N, diff):
    p, q = Ints('p q')
    # z3.Ints(names) - Return a tuple of Integer constants.
    
    s = Solver()
    # z3.Solver() - Init a Solver

    s.add(p > 0, q > 0)
    # Assert constraints into the solver. Solver: [p > 0, q > 0]

    s.add(q*p == N, q-p == diff) 
    # Add new constraints. Solver: [p > 0, q > 0, q * p == <value>, q - p = <value>]

    if s.check() == sat:
        """
        s.check(*assumptions) - Check whether the assertions in 
        the given solver plus the optional assumptions are consistent or not.

        s.check() == sat --> if the specified restrictions have been met 
        """

        m = s.model()
        """
        s.model() - Return a model for the last s.check(). 
        So we get an array like [p = <value>, q = <value>]

        With the values of the constants that satisfies given constraints
        """

        return m[p].as_long(), m[q].as_long()
        # Returning a tuple in the format: (p,q)

    return None


def main():
    f90 = factorial(90)

    diff = f90 - (N % f90) + 1
    # N % f90 : This tells us how far N is from the nearest multiple of 90!
    # f90 - (N % f90) : Gives us the amount needed to add to N to reach the next multiple
    # +1 : Ensures that diff starts from a point that guarantees q > p

    for i in range(200):
        if ( m := solve(N, diff) ):
            break
        diff += f90

    if not m:
        print('Some error occured!')
        return

    p, q = m

    # Default RSA staff
    phi = (p-1) * (q-1)
    d = inverse(E, phi)
    flag = long_to_bytes(pow(C, d, N))

    print(flag.decode())


if __name__ == "__main__":
    main()
# end main
```

