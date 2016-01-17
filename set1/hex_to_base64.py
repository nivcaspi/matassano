import sys

string = ''
try:
  string = sys.argv[1]
except:
  string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

def hex_to_base64(hex_string):
  base64_string = ''
  byte_array = bytearray(hex_string.decode("hex"))

  i=0
  while (i<len(byte_array)):
	print byte_array[i]
	i=i+3

  c = byte_array[0] >> 2
  print c


hex_to_base64(string)
