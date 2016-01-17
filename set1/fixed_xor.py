# fixed xor

def fixed_xor(str1, str2):
  retVal = ''
  ba1 = bytearray(str1.decode("hex"))
  ba2 = bytearray(str2.decode("hex"))

  i=0
  for b1 in ba1:
	retVal += hex(b1 ^ ba2[i])[2:]
	i+=1

  return retVal


print fixed_xor('1c0111001f010100061a024b53535009181c',
'686974207468652062756c6c277320657965')
