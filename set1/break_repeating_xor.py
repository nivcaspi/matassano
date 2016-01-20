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

print get_distance('this is a test', 'wokka wokka!!!')

