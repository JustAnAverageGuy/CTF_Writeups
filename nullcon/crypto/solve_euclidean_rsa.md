
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
