# Break repeating-key XOR

import hex_to_base64
import detect_single_char_xor as scx


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

  return sorted(averaged_distances, key=averaged_distances.get)[:3]


def break_repeating_xor(file1):
    res = []
    f = open(file1)
    line = f.readline()[:60]
    line += f.readline()[:60]
    line = hex_to_base64.base64_to_string(line)
    key_size = guess_key_size(line)[0]
    f.close()
    blocks = []

    for l in open(file1):
      ba1 = bytearray(hex_to_base64.base64_to_string(l[:60]))
      while (len(ba1[:key_size]) == key_size):
        blocks.append(ba1[:key_size])
        ba1 = ba1[key_size:]

    #  if (len(blocks) > 5000):
    #    break

    blocks_t =  map(list, zip(*blocks))

    for ba in blocks_t:
      res.append(scx.xor_most_frequent(ba) + '\n' + 'new line' + '\n')

    return res



#break_repeating_xor('6.txt')
for ba in break_repeating_xor('6.txt'):
    print (str(ba))
#print get_distance('this is a test', 'wokka wokka!!!')
