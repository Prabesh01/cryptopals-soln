from c2 import hex_to_binary, binary_to_hex, xor_binary
import binascii

q="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

frequency_letters=list("ETAOIN SHRDLU")

def score_message(msg):
    score=0
    for char in msg:
        if char in frequency_letters:score+=1
    if (score/len(msg))*100 > 40:
        return True
    else: return False

def binary_to_ascii(x):
    n = int(x, 2)
    return binascii.unhexlify('%x' % n)

    hex_value = '%x' % n
    if len(hex_value) % 2:  # Ensure even length for unhexlify
        hex_value = '0' + hex_value
    return binascii.unhexlify(hex_value).decode('utf-8', errors='ignore')

q_binary=hex_to_binary(q)
# ASCII value of a=97 and z=122
# ASCII value of A=65 and Z=90
loops=[(97,122), (65,90)]
for loop in loops:
    for i in range(loop[0],loop[1]+1): # loop from a to z, A to Z
        key_char=chr(i)
        
        # key=bin(int(str(i),10))[2:]
        key_bin=bin(i)[2:].zfill(8)
        
        xor=""
        for j in range(0,len(q_binary),4):
            four_bit = q_binary[j:j+4]
            xor += xor_binary(key_bin,four_bit.zfill(8))
        
        # method-1:
        message_=binary_to_ascii(xor)
        print(f"{i}-{key_char}: {message_}")

        # method-2:
        # message_hex=binary_to_hex(xor)
        # message=binascii.unhexlify(message_hex)
        # # if score_message(message):
        # print(f"{i}-{key_char}: {message}")

