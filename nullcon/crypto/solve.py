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