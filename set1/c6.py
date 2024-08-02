from c4 import get_remote_content
from c3 import decode_single_byte_xor, score_message
from c5 import decode_repeating_key_xor
import base64

q=get_remote_content('https://cryptopals.com/static/challenge-data/6.txt')
q=base64.b64decode(q)

t1=b"this is a test"
t2=b"wokka wokka!!!"

def calc_ham_dis(a,b):
    assert len(a) == len(b)
    assert type(a) == type(b) == type(bytes())

    diff = 0
    for i in range(len(a)):
        xor = a[i] ^ b[i]
        diff += bin(xor).count('1')

    return diff

def figure_key_size_2(q):
    lowest_diff=float('inf')
    KEYSIZE = None

    for size in range(2,51):
        if size>(len(q)/2): continue
        for i in range(1,int(len(q)/size)):
            first_chunk = q[0+i:size+i]
            second_chunk = q[size+i:size*2+i]
            diff = calc_ham_dis(first_chunk, second_chunk)
            normalized_diff = diff/size
            if normalized_diff<lowest_diff:
                lowest_diff=normalized_diff
                KEYSIZE=size
    
    return KEYSIZE

def figure_key_size(q):
    lowest_diff = float('inf')
    best_keysize = None
    
    # We will check a range of sizes and use more data for each size
    for size in range(2, 51):
        diffs = []
        # Use multiple segments for each key size to improve accuracy
        for start in range(0, len(q) - size*2 + 1, size):
            segment1 = q[start:start+size]
            segment2 = q[start+size:start+size*2]
            if len(segment1) == size and len(segment2) == size:
                diff = calc_ham_dis(segment1, segment2)
                normalized_diff = diff / size
                diffs.append(normalized_diff)
        
        if diffs:
            avg_diff = sum(diffs) / len(diffs)
            if avg_diff < lowest_diff:
                lowest_diff = avg_diff
                best_keysize = size
    
    return best_keysize

def create_block(s,n):
    block=[]
    i=0
    while(i<len(s)):
        block.append(s[i:i+n])
        i+=n
    return block

def transpose_block(block):
    transposed = [[] for b in block[0]]

    for b in block:
        for i in range(len(b)):
                transposed[i].append(b[i])
    assert len(block) ==  len(transposed[0])
    return transposed

def display_solution(keysize, key, pt):
    print(f"KEYSIZE: {keysize}")
    print("key: "+repr(key))
    print("PlainText:")
    print(pt)

assert calc_ham_dis(t1,t2) == 37

test_list = [
    "a","b","c","d","e","f",
    "a","b","c","d","e","f",
    "a","b","c","d","e","f",
    "a","b","c","d","e","f",
    "w"]
test_blocks=create_block(test_list, 6)
assert test_blocks == [
    ["a","b","c","d","e","f"],
    ["a","b","c","d","e","f"],
    ["a","b","c","d","e","f"],
    ["a","b","c","d","e","f"],
    ["w"]
]

transposed_blocks=transpose_block(test_blocks)
assert transposed_blocks == [
    ["a","a","a","a","w"],
    ["b","b","b","b"],
    ["c","c","c","c"],
    ["d","d","d","d"],
    ["e","e","e","e"],
    ["f","f","f","f"]
]

if __name__=="__main__":
    KEYSIZE = figure_key_size(q) 

    blocks_of_keysize=create_block(q, KEYSIZE)
    transposed_blocks = transpose_block(blocks_of_keysize)

    key=""
    for block in transposed_blocks:
        key+=decode_single_byte_xor(block, display=False)

    display_solution(KEYSIZE, key, decode_repeating_key_xor(q, key))

    # key_dict={}
    # for KEYSIZE in range(2,51):
    #     blocks_of_keysize=create_block(q, KEYSIZE)

    #     transposed_blocks = transpose_block(blocks_of_keysize)
        
    #     key_dict[str(KEYSIZE)]=""
            
    #     for block in transposed_blocks:
    #         key=decode_single_byte_xor(block, display=False)
    #         if key: key_dict[str(KEYSIZE)]+=key
        
    # for key_size, key in key_dict.items():
    #     if score_message(key):
    #         print(key_size)
    #         print(key)
    #         display_solution(key_size, key, decode_repeating_key_xor(q, key))
