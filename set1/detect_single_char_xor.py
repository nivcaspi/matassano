# detect single char xor

import single_byte_xor as sbx


def xor_most_frequent(ba1):
  most_frequent = sbx.find_most_frequent(ba1)
  key = 32 ^ most_frequent

  return sbx.single_byte_xor(ba1, key)

def is_english(ba):
  count=0

  for b in ba:
    if (b > 64 and b < 91):
      count += 1
    elif (b > 96 and b < 123):
      count += 1
    elif (b == 32 or b == 10):
      count += 1

  percent = count*100/len(ba)
  if (percent > 90):
    return True
  else:
    return False


def break_single_byte_xor(file1):
  f = open(file1)
  decrypt = ''
  i = 0

  for l in f:
    if (len(l) % 2 != 0):
      l = l[:(len(l)-1)]

    l = l.decode('hex')
    l = bytearray(l)
    decrypt = xor_most_frequent(l)

    if (is_english(decrypt)):
      return decrypt

    i+=1
  return 'could not decipher'



#print break_single_byte_xor('4.txt')
