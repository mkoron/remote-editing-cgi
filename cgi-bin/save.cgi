#!/usr/bin/env python3

print("Content-type: text/html\n")

from os.path import join, abspath
import cgi, hashlib, sys

BASE_DIR = abspath('data')
CHECK_PASS = 'bd2b1aaf7ef4f09be9f52ce2d8d599674d81aa9d6a4421696dc4d93dd0619d682ce56b4d64a9ef097761ced99e0f67265b5f76085e5b0ee7ca4696b2ad6fe2b2'

form = cgi.FieldStorage()

text = form.getvalue('text')
filename = form.getvalue('filename')
password = form.getvalue('password')

if not (filename and text and password):
    print('Error, invalid parameters')
    sys.exit()

hashed_password = hashlib.sha512(password.encode()).hexdigest()

if hashed_password != CHECK_PASS:
    print('Invalid password!')
    sys.exit()

f = open(join(BASE_DIR, filename), 'w')
f.write(text)
f.close()

print("The file has been saved.")