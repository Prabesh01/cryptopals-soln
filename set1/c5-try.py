q1="Burning 'em, if you ain't quick and nimble"
q2="""
I go crazy when I hear a cymbal"""

a1="0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
a2="a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

repeating_key="ICE"

def encode_repeating_key_xor(pt, key, index=0):
    len_key=len(key)

    list_pt=list(pt)
    len_pt=len(list_pt)

    ct=bytearray(len_pt)
    for i in range(len_pt):
        key_index = index%len_key
        key_char = key[key_index]  
        ct[i]=ord(list_pt[i]) ^ ord(key_char)
        index+=1
    return ct.hex()

if __name__=="__main__":
    hex1 = encode_repeating_key_xor(q1, repeating_key) 
    print(hex1)
    print(a1)
    print('----')
    hex2 = encode_repeating_key_xor(q2, repeating_key, len(q1))
    print(hex2)
    print(a2)
    print('----')
    print(hex1+hex2 == a1+a2)

