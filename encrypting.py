# make sure PyCrypto using pip

import codecs
from base64 import b64encode, b64decode

from Crypto.Cipher import ARC4

key = b'%'
plain = b"this is a secret"

cipher = ARC4.new(key)
msg = cipher.encrypt(plain)

print("the encrypted message: %s" %  msg)
print("and we'll transmit it as base64: %s" % b64encode(msg))
