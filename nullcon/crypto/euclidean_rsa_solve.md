# Euclidean RSA

## <u>Challenge Description</u>

> Bob apparently likes squares, but what does it have to do with encryption?

<details>
<summary> <h3>Challenge Files</h3> </summary>

> [euclidean-rsa.py](euclidean_RSA.py)

```py
#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long
from secret import flag, magic

while True:
    try:
        key = RSA.generate(2048)
        a,b,c,d = magic(key)
        break
    except:
        pass
assert a**2 + b**2 == key.n
assert c**2 + d**2 == key.n
for _ in [a,b,c,d]:
    print(_)
cipher = pow(bytes_to_long(flag), key.e, key.n)
print(cipher)
```

> [output.txt](output.txt)
</details>
<details>
<summary> <h3> Hint(s) </h3> </summary>

Observe that $\left(a^2 + b^2\right) \cdot \left(c^2 + d^2\right) $ can always be
represented as $P^2 + Q^2$ for determinable $P, Q$.
</details>

---

<details>
<summary> <h3> Solution </h3> </summary>

We have representation of $n$ as a sum of two squares in two different ways and
we need to use it to find the factors.

Let me show a fun property of sum of two squares : )

Call a number happy if it is a sum of two square integers,
then, product of happy numbers is also happy.

Let $p,q$ be two happy numbers.
In particular, let $p = k^2 + l^2, q =  r^2 + s^2$

$$
\begin{align}
p\cdot q &= (k^2 + l^2)\cdot (r^2 + s^2)\nonumber\\
         &= (kl)^2 + (kr)^2 +(lr)^2 + (ls)^2\nonumber\\
         &= (kr)^2 + (ks)^2 +(lr)^2 + (ls)^2 - 2(kr)(ls) + 2(ks)(lr)\\
         &= [(kr)^2 + (ls)^2 - 2(kr)(ls)] + [(ks)^2 +(lr)^2 + 2(ks)(lr)]\nonumber\\
         &= (kr - ls)^2 + (ks+lr)^2\\

&\text{Also, (1) can also be rearranged as follows}\nonumber\\

         &= [(kr)^2 + (ls)^2 + 2(kr)(ls)] + [(ks)^2 +(lr)^2 - 2(ks)(lr)]\nonumber\\
         &= (kr + ls)^2 + (ks-lr)^2
\end{align}

$$
Hence $(2), (3)$ show that product of two happy numbers is happy,
at least in two ways !

This matches our problem.

If we let
$$\begin{align}
kr-ls &= a\\
ks+lr &= b\\
&\nonumber\\
kr+ls &= c\\
ks-lr &= d\\
\end{align}
$$
Then,

$(4) + (6) \implies kr = (a+c)/2$

$(5) + (7) \implies ks = (b+d)/2$

Also if $q = r^2 + s^2$ is prime then $\gcd(r,s) = 1$
since $\gcd(r,s)^2 \text{ divides } q$.

Therefore $\gcd(kr,ks) = k\cdot\gcd(r,s) = k$

Similarly, we also get $l$ by considering $(4) - (6)$ and $(5) - (7)$.

Having $k$ and $l$, we obtain $p = k^2 + l^2$, and boom, we are done !.
</details>

<details>
<summary><h3>Solution Script</h3></summary>

[solve.py](solve.py)

```py
with open("./output.txt") as f: a,b,c,d,enc = map(int,f.readlines()) 

from math import gcd

n = a*a + b*b

kr = (a+c)//2 
ks = (b+d)//2

k = gcd(kr,ks)

r = kr//k
s = ks//k

q = r*r + s*s

p = n // q

# standard RSA decryption ahead
phi = n-p-q+1
d = pow(65537, -1 ,phi)
print(pow(enc,d,n).to_bytes(60,"big").decode())

# ENO{Gauss_t0ld_u5_th3r3_1s_mor3_th4n_on3_d1men5i0n}
```

</details>
