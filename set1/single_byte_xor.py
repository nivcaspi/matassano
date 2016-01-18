# single byte xor cipher

def single_byte_xor(str1, char):
  retVal = ''
  ba1 = bytearray(str1.decode("hex"))

  for b in ba1:
      retVal += chr(b ^ ord(char))

  return retVal


print single_byte_xor('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736', chr(88))
