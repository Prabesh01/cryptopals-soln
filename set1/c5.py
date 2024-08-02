q="""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

a="""0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""

repeating_key="ICE"

def encode_repeating_key_xor(pt, key):
    len_key=len(key)

    list_pt=list(pt)
    len_pt=len(list_pt)

    ct=bytearray(len_pt)
    for i in range(len_pt):
        key_char = key[i%len_key]  
        ct[i]=ord(list_pt[i]) ^ ord(key_char)
    return ct.hex()

def decode_repeating_key_xor(ct, key):
    len_key=len(key)

    list_ct=list(ct)
    len_ct=len(list_ct)

    pt=bytearray(len_ct)
    for i in range(len_ct):
        key_char = key[i%len_key]  
        pt[i]=list_ct[i] ^ ord(key_char)
    return pt.decode('utf-8')


if __name__=="__main__":
    print(encode_repeating_key_xor(q, repeating_key) == a)
