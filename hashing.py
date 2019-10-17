import codecs
from base64 import b64encode, b64decode
from hashlib import md5


unprintable_bytes = b"hello world \x81"
unprintable_bytes_hex = codecs.encode(unprintable_bytes, "hex")
unprintable_bytes_b64 = b64encode(unprintable_bytes)
d = md5()
d.update(unprintable_bytes)
h = d.digest()


print("unprintable_bytes is equal to: %s" % unprintable_bytes)
print("we can represent these as hex: %s" % unprintable_bytes_hex)
print("but base64 encoded it is represented as: %s" % unprintable_bytes_b64)
print("we can then decode the base64 representation: %s" % b64decode(unprintable_bytes_b64))
print("the md5 hash of unprintable_bytes is: %s" % h)
print("usually, we pass hashes in ascii: %s" % codecs.encode(h, "hex"))
