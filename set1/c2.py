q1="1c0111001f010100061a024b53535009181c"
q2="686974207468652062756c6c277320657965"
a="746865206b696420646f6e277420706c6179"

hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

reversed_hex_dict = {value: key for key, value in hex_dict.items()}

def pad_binary_with_leading_zero(hex_str,bin_str):
    required_length=len(hex_str)*4
    return bin_str.zfill(required_length)

def hex_to_binary(x):
    # method-1:
    # binary=""
    # for c in x:
    #     binary+=hex_dict[c]
    # return binary 

    # method-2:
    binary = bin(int(x,16))[2:] # remove 0b
    return pad_binary_with_leading_zero(x,binary)

def binary_to_hex(x):
    # method-1:
    # hex=""
    # for i in range(0,len(x),4):
    #     four_bit = x[i:i+4]
    #     hex += reversed_hex_dict[four_bit]
    # return hex

    # method-2:
    return hex(int(x, 2))[2:] # remove 0x

def xor_binary(x,y):
    x=str(x)
    y=str(y)
    if len(x)!=len(y): 
        print("equal-length buffers required!")
        return

    # method-1:
    xor=""
    for i in range(len(x)):
        if x[i]==y[i]:
            xor+="0"
        else:
            xor+="1"
    return xor

    # method-2:
    # xor=int(x,2) ^ int(y,2)
    # return bin(xor)[2:].zfill(len(x))

if __name__==  '__main__':
    q1_binary, q2_binary = hex_to_binary(q1), hex_to_binary(q2)
    binary_XOR=xor_binary(q1_binary, q2_binary)
    print(binary_to_hex(binary_XOR) == a)
