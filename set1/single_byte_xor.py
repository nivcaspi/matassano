# single byte xor cipher

def single_byte_xor(ba1, char):
  resBa = bytearray()
  for b in ba1:
      resBa.append(b ^ char)

  return resBa

def find_most_frequent(ba1):
    d = {}
    for b in ba1:
      d[b] = 0

    for b in ba1:
        d[b] = d[b]+1

    f = sorted(d, key=d.get)
    return f[len(f)-1]

#str2 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#print (single_byte_xor(str2, chr(ord(' ') ^ find_most_frequent(str2))))
