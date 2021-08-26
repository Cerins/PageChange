import hashlib
import urllib.request
import sys

LOCAL_HASH_FILE = 'hash'
URL = 'http://someurl'


if(len(sys.argv) != 2):
    raise ValueError('Invalid amount of args given')

if(sys.argv[1] == 'store'):
    remote_data = urllib.request.urlopen(URL).read()
    remote_hash = hashlib.md5(remote_data).hexdigest()

    with open(LOCAL_HASH_FILE, 'w') as f:
        f.write(remote_hash)

    print('Local hash stored')

elif(sys.argv[1] == 'check'):
    remote_data = urllib.request.urlopen(URL).read()
    remote_hash = hashlib.md5(remote_data).hexdigest()

    local_hash = open(LOCAL_HASH_FILE, 'r').read()

    if(remote_hash == local_hash):
        print("Webpage didn't change")
    else:
        print("Webpage changed")


else:
    raise ValueError(f"Invalid argument - {sys.argv[1]}")

