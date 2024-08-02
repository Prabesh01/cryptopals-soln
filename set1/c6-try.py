from c2 import xor_binary

t1="this is a test"
t2="wokka wokka!!!"

def calc_ham_dis(a,b):
    assert len(a) == len(b)

    xor=0
    for i in range(len(a)):
        xor += ord(a[i]) ^ ord(b[i])
        # xor += a[i] ^ b[i]

    diff = 0
    for c in str(xor):
        diff += int(c)
    return diff

print(calc_ham_dis(t1,t2))
