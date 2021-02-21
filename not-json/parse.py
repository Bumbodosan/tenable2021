import base64
import bson

f = open("input.txt")
b64 = base64.b64decode(f.read())
f.close()

data = bson.loads(b64)

alphabet = data.get("0")
indexes = data.get("1")

flag = "".join(map(lambda index: alphabet[index], indexes))

print(flag)