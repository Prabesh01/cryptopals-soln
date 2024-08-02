from c3 import decode_single_byte_xor
import urllib.request
from c5 import encode_repeating_key_xor
import os

q="https://cryptopals.com/static/challenge-data/4.txt"


CACHE_PATH=os.path.dirname(os.path.abspath(__file__))+"/../downloads/"
if not os.path.exists(CACHE_PATH):os.makedirs(CACHE_PATH)

def cache_file(url):
    file_name=encode_repeating_key_xor(url,"MY_KEY")
    if not os.path.exists(CACHE_PATH+file_name):
        try:
            response = urllib.request.urlopen(url)
            data = response.read()
            with open(CACHE_PATH+file_name,"wb") as f:
                f.write(data)
        except:
            return False
    return file_name

def get_remote_content(url):
    file_name = cache_file(url)
    if file_name: return open(CACHE_PATH+file_name,'r').read()
    else: return ""

if __name__=="__main__":

    sixty_char_strings = get_remote_content(q).splitlines()

    for string in sixty_char_strings:
        decode_single_byte_xor(bytes.fromhex(string))
