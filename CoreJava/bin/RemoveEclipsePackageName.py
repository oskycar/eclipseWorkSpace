#!/usr/bin/python
"""
remove the package name that added by python scripts
You must have Python 2.3 installed to run this program. See www.python.org.
"""
import os

for path, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(".java"):
            filepath = path + os.sep + file
            code = open(filepath).readlines()
            found = False
            for n, line in enumerate(code):
                if line.find(" /* Added by AddEclipsePackageName.py */") != -1:
                    del code[n]
            open(filepath, 'w').writelines(code)
