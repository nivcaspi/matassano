# repeating key xor

def repeating_xor(str1, key):
    ba1 = bytearray(str1, 'utf-8')
    ba2 = bytearray(key, 'utf-8')
    val = ''

    i = 0
    while (i <  len(ba1)):
        for b in (ba2):
            if (i < len(ba1)):
                #print (chr(ba1[i]), ' xor ', chr(b))
                #print (hex(ba1[i] ^ b), len(hex(ba1[i] ^ b)))
                val += '0' if (len(hex(ba1[i] ^ b))==3) else ''
                val += str((hex((ba1[i]) ^ b))[2:])
                i += 1

    return val


str2 = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
print (repeating_xor(str2, 'ICE'))
