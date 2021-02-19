import ecdsa
import random
from Crypto.Cipher import AES
import binascii

def pad(m):
    return m+chr(16-len(m)%16)*(16-len(m)%16)

G = ecdsa.NIST256p.Gerator
order = G.order()
priv = random.randrange(1,order)
 
pub_key = ecdsa.ecdsa.Public_key(G, G * priv)
priv_key = ecdsa.ecdsa.Private_key(pub_key, priv)
 
k = random.randrange(1, 2**127)
k1 = k
 
# randomly Gerate hash value
hash1 = random.randrange(1, order)
hash2 = random.randrange(1, order)
 
sig1 = priv_key.sign(hash1, k)
sig2 = priv_key.sign(hash2, k1)

s1 = sig1.s
s2 = sig2.s

print("r: " + str(sig1.r))
print("s1: " + str(s1))
print("s2: " + str(s2))
print("")
print("hashes:")
print(hash1)
print(hash2)
print("")
print("order: " + str(order))
print("")

aes_key = priv.to_bytes(64, byteorder='little')[0:16]

ptxt =  pad("flag{example}")
IV = b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'
cipher = AES.new(aes_key, AES.MODE_CBC, IV)
ctxt = cipher.encrypt(ptxt.encode('utf-8'))

print("Encrypted Flag:")
print(binascii.hexlify(ctxt))
