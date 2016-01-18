# detect single char xor

import single_byte_xor as sbx


f = open('4.txt')
i = 0
for l in f:
    line = l[:60]
    if (len(line)%2 ==0):
        char = sbx.find_most_frequent(line)
        print str(i) + ' ' + sbx.single_byte_xor(line, chr(ord(' ') ^ char))
    else:
        print 'odd line here'
        print str(i) + ' ' + line
    i+=1


