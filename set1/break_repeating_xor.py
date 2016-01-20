# Break repeating-key XOR

def count_bits(byte):
    #return bin(byte).count('1')
    byte = (byte & 0x55) + ((byte >> 1) & 0x55)
    byte = (byte & 0x33) + ((byte >> 2) & 0x33)
    byte = (byte & 0x0f) + ((byte >> 4) & 0x0f)
    return byte

def get_distance(str1, str2):
    result = 0
    ba1 = bytearray(str1)
    ba2 = bytearray(str2)

    for b1, b2 in zip(ba1, ba2):
        result += count_bits(b1 ^ b2)

    return result

def guess_key_size(str1):
  max_key_size = 40 if (len(str1) > 80) else (len(str1) / 2 + 2)
  key_sizes = xrange(2, max_key_size)
  averaged_distances = {}

  for s in key_sizes:
    s1 = str1[:s]
    s2 = str1[:(s*2)][s:]


    averaged_distances[s] = float(get_distance(s1, s2)) / float(s)

  return sorted(averaged_distances, key=averaged_distances.get)[:2]


def break_repeating_xor(file1):
    res = ''
    f = open(file1)
    key_size = guess_key_size(f.read()[:90])
    f.close()
    blocks = []

    for l in open(file1):
      blocks += bytearray(l)





    return res



print break_repeating_xor('C:/Users/niv.caspi/Projects/matassano/set1/6.txt')

