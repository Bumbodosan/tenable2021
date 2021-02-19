import re

values = [None, "GED\x03hG\x15&Ka =;\x0c\x1a31o*5M"]

DRX = 0
TRX = 1

f = open("crypto.asm")

def indexfromvariable(variable):
  index = -1
  if variable == "DRX":
    index = DRX
  elif variable == "TRX":
    index = TRX
  else: 
    print("Index is", index, "for", variable)
    exit(1)
  return index

def mov(index, value): 
  match = re.match("\".*\"", value);
  if match: values[index] = value[match.pos + 1 : match.endpos - 1]
  else: values[index] = values[indexfromvariable(value)]

def reverse(index):
  values[index] = str(values[index])[::-1]

def xor(f, s):
  fv = values[f]
  sv = values[s];
  length = len(fv);
  l = "".join([chr(ord(a) ^ ord(b)) for a,b in zip(fv, sv)])
  if len(l) < length:
    l += fv[len(l):length]
  values[f] = l
  
for line in f.read().splitlines():
  split = line.split(" ")
  operation = split.pop(0)
  if operation == "MOV": 
    variable = indexfromvariable(split.pop(0))
    value = split.pop(0)
    mov(variable, value)
  elif operation == "REVERSE":
    variable = indexfromvariable(split.pop(0))
    reverse(variable)
  elif operation == "XOR":
    first = indexfromvariable(split.pop(0))
    second = indexfromvariable(split.pop(0))
    xor(first, second)

print(values[TRX])

# flag{N1ce_Emul8tor!1}
