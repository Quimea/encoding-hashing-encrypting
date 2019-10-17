import codecs
from base64 import b64encode, b64decode

unprintable_bytes = b"hello world \x81"
unprintable_bytes_hex = codecs.encode(unprintable_bytes, "hex")
unprintable_bytes_b64 = b64encode(unprintable_bytes)

print("unprintable_bytes is equal to: %s" % unprintable_bytes)
print("we can represent these as hex: %s" % unprintable_bytes_hex)
print("but base64 encoded it is represented as: %s" % unprintable_bytes_b64)
print("we can then decode the base64 representation: %s" % b64decode(unprintable_bytes_b64))
