from Crypto.Util.number import inverse
from Crypto.Cipher import AES
from binascii import unhexlify

'''
This is the exat vulnerability mentioned in the ECDSA wikipedia article: https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm
Basically since k is the same => r is the same => 2 equations and 2 unknowns => totally broken crypto! 
'''

# signatures (r, s1) and (r, s2)
r = 50394691958404671760038142322836584427075094292966481588111912351250929073849
s1 = 26685296872928422980209331126861228951100823826633336689685109679472227918891
s2 = 40762052781056121604891649645502377037837029273276315084687606790921202237960

# hashes
z1 = 777971358777664237997807487843929900983351335441289679035928005996851307115
z2 = 91840683637030200077344423945857298017410109326488651848157059631440788354195

# Curve order (n)
order = 115792089210356248762697446949407573529996955224135760342422259061068512044369

# Encrypted Flag:
enc_flag = unhexlify(b'f3ccfd5877ec7eb886d5f9372e97224c43f4412ca8eaeb567f9b20dd5e0aabd5')

k = (((z1 - z2) % order) * inverse(s1 - s2, order)) % order
priv = ((((s1 * k) % order) - z1) * inverse(r, order)) % order

aes_key = priv.to_bytes(64, byteorder='little')[0:16]
IV = b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'
cipher = AES.new(aes_key, AES.MODE_CBC, IV)

print(cipher.decrypt(enc_flag))
# flag{cRypt0_c4r3fully}
