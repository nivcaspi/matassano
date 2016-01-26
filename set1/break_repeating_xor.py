# Break repeating-key XOR

import hex_to_base64
import detect_single_char_xor as scx
import pdb

def count_bits(byte):
    byte = (byte & 0x55) + ((byte >> 1) & 0x55)
    byte = (byte & 0x33) + ((byte >> 2) & 0x33)
    byte = (byte & 0x0f) + ((byte >> 4) & 0x0f)

    return byte

def get_distance(ba1, ba2):
    result = 0

    for b1, b2 in zip(ba1, ba2):
        result += count_bits(b1 ^ b2)

    return result

def guess_key_size(ba1):
    max_key_size = 40 if (len(ba1) > 80) else (len(ba1) / 2 + 2)
    key_sizes = xrange(2, max_key_size)
    averaged_distances = {}

    for s in key_sizes:
      ba2 = ba1[:s]
      ba3 = ba1[:(s*2)][s:]
      averaged_distances[s] = float(get_distance(ba2, ba3)) / float(s)
    return sorted(averaged_distances, key=averaged_distances.get)[:3]

def break_repeating_xor(b64_ba):
    res = []
    #ba1 = bytearray(hex_to_base64.base64_to_string(b64_ba))
    ba1 = bytearray(hex_to_base64.b64_to_str(b64_ba))
    key_size = guess_key_size(ba1)[0]
    blocks = []

    while (len(ba1[:key_size]) == key_size):
      blocks.append(ba1[:key_size])
      ba1 = ba1[key_size:]

    blocks_t =  map(list, zip(*blocks))

    for ba in blocks_t:
      res.append(scx.xor_most_frequent(ba, ord(' ')) + '\n' + 'new line' + '\n')

    return res



with open('6.txt', 'rb') as f:
  for l in break_repeating_xor(f.read()):
	print str(l)

