import codecs
from base64 import b64encode, b64decode

msg = b'jBZih4F3FJJ2qLddnR/Gvw=='
key = b'%'

cipher = ARC4.new(key)
msg = cipher.decrypt(b64decode(msg))

print("the encrypted message: %s" %  msg)
