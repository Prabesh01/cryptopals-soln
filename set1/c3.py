import string

ct = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

frequency_letters=list("ETAOIN SHRDLU")
printable_chars = set(string.printable)
def score_message(msg):
    if not ' ' in msg.strip(): return False
    if not msg.strip(): return False
    score=0
    for char in msg:
        if char in frequency_letters:score+=1
    if (score/len(msg))*100 > 13 and all(char in printable_chars for char in msg):
        return True
    else: return False

frequency_dict={"E":12.7,"I":6.97,"R":5.99,"U":2.76,"G":2.02,"V":0.98,"Q":0.095,"T":9.06,"N":6.75,"D":4.25,"M":2.41,"Y":1.97,"K":0.77,"Z":0.074,"A":8.17,"S":6.33,"L":4.02,"W":2.36,"P":1.93,"J":0.15}
def score_message_2(msg):
    if not ' ' in msg: return False
    score=0
    for char in frequency_dict:
        if char.upper() in frequency_dict:score+=frequency_dict[char.upper()]
    return True if score>60 else False

def decode_single_byte_xor(ct,display=True):
    for i in range(256):
        pt=bytearray(len(ct))
        for j in range(len(ct)):
            pt[j]=ct[j] ^ i
        try:
            msg=pt.decode('utf-8')
            if score_message(msg):
                if display:
                    print(f"{i}-{chr(i)}: {pt}")
                return chr(i)
        except: pass

if __name__==  '__main__':
    decode_single_byte_xor(bytes.fromhex(ct))

    # decode_single_byte_xor(bytes.fromhex("7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f"))