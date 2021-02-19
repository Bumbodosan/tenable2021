import requests
from Crypto.Cipher import AES
from base64 import b64decode

'''
This is a textbook example of "byte-at-a-time ECB decryption." 
We can send a request to the challange server with a string of our choosing, the server appends the flag and it all gets encrypted under an unknown but fixed key and we recieve back the resulting encrypted string. 
We can also see that they add some PKCS_7 padding which means we do not have to worry about dealing with the message being too long or too short compared to the block-length of 16 bytes. 
Let us imagine we send 15 bytes of data to the server, in python using "a" * 15 The server will append the flag resulting in the first encrypted block consisting of 15 known characters and the first character of the flag. Call this C1. 
We can assume the flag consists of ascii-characters which means there are only 128 possibilities for the unknown character. (Practically speaking there are less since not all characters in ascii are relevant)
Now we can create a dictionary mapping all 128 different ciphertext possibilites to the 128 possible characters and simply choose the character corresponding to C1. 
This process is then repeated for the entire flag but for each discovered character we reduce the number of "a"s we send until we have an entire block, then repeating this for every block:

send "a" * 15 -> get flag1
send "a" * 14 + flag1 -> get flag2
...
send flag[0 : 15] -> get flag16
send "a" * 15 -> get flag17
etc
'''

def create_dict(start_index, known_bytes, blocksize = 16):
    di = {}
    for i in range(128):
        post_params = {
            "text_to_encrypt": b"a" * (15 - len(known_bytes)) + known_bytes + bytes([i]),
            "do_encrypt": "Encrypt"
        }
        r = requests.post("http://167.71.246.232:8080/crypto.php", data=post_params)
        resp = r.text
        encrypted = b64decode(bytes(resp[resp.find("Encrypted Data:</h2><br/><b>") + len("Encrypted Data:</h2><br/><b>") : -len("</b></body></html>") - 2], "ascii"))[ : 16]
        di[encrypted] = bytes([i])
    return di


seen = b""
for i in range(0, 10000, 16):
    for j in range(16):
        post_params = {
            "text_to_encrypt": b"a" * (15 - j),
            "do_encrypt": "Encrypt"
        }

        r = requests.post("http://167.71.246.232:8080/crypto.php", data=post_params)
        resp = r.text
        encrypted = b64decode(bytes(resp[resp.find("Encrypted Data:</h2><br/><b>") + len("Encrypted Data:</h2><br/><b>") : -len("</b></body></html>") - 2], "ascii"))[i : i + 16]
        d = create_dict(i, seen[-15 : ])
        seen += d[encrypted]
        # print(encrypted)
        # print(d)
        print(seen)

# flag{b4d_bl0cks_for_g0nks}
