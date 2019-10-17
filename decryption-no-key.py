from Crypto.Cipher import ARC4
import codecs
from base64 import b64encode, b64decode

for i in range(256):
  cipher = ARC4.new((bytes([i])))
  msg = cipher.decrypt(b64decode(b'jBZih4F3FJJ2qLddnR/Gvw=='))
  print("The secret message is: %s" % msg)
