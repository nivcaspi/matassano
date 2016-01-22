# convert hex to base64

def sixete_to_base64(six):
  if (six < 26):
    return unichr(six+65)#A-Z
  elif (six < 52):
    return unichr(six+71)#a-z
  elif (six < 62):
    return unichr(six-4)#0-9
  elif (six == 62):
    return unichr(43)#+
  elif (six == 63):
    return unichr(47)#/
  elif (six == 64):
    return unichr(61)#=
  else:
    return unichr(42)#*

def base64_to_sixete(b64):
  b64 = ord(b64)

  if (b64 == 43):#+
    return format(62, '06b')
  elif (b64 == 47):#/
    return format(63, '06b')
  elif (b64 < 58):#0-9
    return format(b64 + 4, '06b')
  elif (b64 == 61):#=
    return ''
  elif (b64 < 91):#A-Z
    return format(b64 - 65, '06b')
  elif (b64 < 123):#a-z
    return format(b64 - 71, '06b')
  else:
    return b64 + ' is not a base64 char'

def hex_to_base64(hex_string):
  retVal = ''
  ba = bytearray(hex_string.decode("hex"))
  i=0

  while (i < len(ba)):
    a = (ba[i] >> 2)
    b = (ba[i] & 3) << 4
    # 3 bytes to the end
    if ((i+2) < len(ba)):
      b |= (ba[i+1] >> 4)
      c = ((ba[i+1] & 15) << 2) | (ba[i+2] >> 6)
      d = ba[i+2] & 63
      # 2 bytes to the end
    elif ((i+1) < len(ba)):
      b |= (ba[i+1] >> 4)
      c = ((ba[i+1] & 15) << 2)
      d = '='
    # 1 byte to the end
    else:
      c = '='
      d = '='

    i=i+3

    retVal += (sixete_to_base64(a) + sixete_to_base64(b) + sixete_to_base64(c)
		+ sixete_to_base64(d))

  return retVal

def base64_to_string(b64_str):
    bin_str = ''
    res = ''

    for c in b64_str:
        bin_str += base64_to_sixete(c)

    while (bin_str):
        res += chr(int(bin_str[:8], 2))
        if(len(bin_str)>=8):
            bin_str = bin_str[8:]
        else:
            bin_str = None

    return res


'''
hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print hex_to_base64(hex_str)
b64_str = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
print base64_to_string(b64_str)
'''
