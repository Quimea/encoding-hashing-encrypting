# encoding-hashing-encrypting
Explanations of all three, with examples of each in Python.


# Encoding
The process of transforming data such that it is recoverable by anyone without a key
Base 64 is a binary encoding schema that allows for turning unprintable binary data into ASCII text. Encoding makes the transmission of data possible for systems that can't speak unprintable characters, for example.
Below, you can update unprintable bytes to whatever string of characters you like, or you can use the example given.
``` python
import codecs
from base64 import b64encode, b64decode

unprintable_bytes = b"hello world \x81"
unprintable_bytes_hex = codecs.encode(unprintable_bytes, "hex")
unprintable_bytes_b64 = b64encode(unprintable_bytes)

print("unprintable_bytes is equal to: %s" % unprintable_bytes)
print("we can represent these as hex: %s" % unprintable_bytes_hex)
print("but base64 encoded it is represented as: %s" % unprintable_bytes_b64)
print("we can then decode the base64 representation: %s" % b64decode(unprintable_bytes_b64))
```
The result of the above runned is below:
```
unprintable_bytes is equal to: b'hello world \x81'
we can represent these as hex: b'68656c6c6f20776f726c642081'
but base64 encoded it is represented as: b'aGVsbG8gd29ybGQggQ=='
we can then decode the base64 representation: b'hello world \x81'
```
