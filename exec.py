import sys
import hashlib
import binascii
import os
import base64
import re

password = "blah"
salt = "blah"

exec sys.argv[1]
dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
hashed_input = binascii.hexlify(dk)
print hashed_input