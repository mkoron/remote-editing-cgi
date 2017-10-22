#!/usr/bin/env python3

print("Content-type: text/html\n")

from os.path import join, abspath
import cgi, sys

BASE_DIR = abspath('data')

form = cgi.FieldStorage()
filename = form.getvalue('filename')
if not filename:
    print('Please enter a file name')
    sys.exit()

with open(join(BASE_DIR, filename), 'r') as input:
    text = input.read()

print("""
<html>
    <head>
        <title>Edit File</title>
    </head>
    <body>
        <form action='save.cgi' method='POST'>
        <b>File name:</b> {}<br>
        <input type='hidden' value='{}' name='filename'>
        <b>Password:</b><br>
        <input name='password' type='password'><br>
        <b>Text:</b><br>
        <textarea name='text' cols='60' rows='40'>{}</textarea><br>
        <input type='submit' value='Save'>
        </form>
    </body>
</html>
""".format(filename, filename, text))