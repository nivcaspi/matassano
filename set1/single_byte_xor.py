# single byte xor cipher

def single_byte_xor(str1, char):
  retVal = ''
  ba1 = bytearray(str1.decode("hex"))

  for b in ba1:
      retVal += chr(b ^ ord(char))

  return retVal

def find_most_frequent(str1):
    ba1 = bytearray(str1.decode('hex'))
    d = {}

    for b in ba1:
      d[b] = 0

    for b in ba1:
        d[b] = d[b]+1

    f = sorted(d, key=d.get)
    return f[len(f)-1]

#str2 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#print single_byte_xor(str2, chr(ord(' ') ^ find_most_frequent(str2)))
