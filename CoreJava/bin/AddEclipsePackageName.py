#!/usr/bin/python
"""
add package name for the java file in that dirs
You must have Python 2.3 installed to run this program. See www.python.org.
"""
import os

for path, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(".java"):
            filepath = path + os.sep + file
            filepath = filepath[2:]
            tagPath = ".".join(filepath.split('\\')[:-1])
            packageStatement = "package " + tagPath + ";"
            code = open(filepath).readlines()
            found = False
            for n, line in enumerate(code):
                if line.startswith("package "):
                    del code[n]
                    found = False
            if not found:
                code.insert(0, packageStatement + " /* Added by AddEclipsePackageName.py */\n")
                open(filepath, 'w').writelines(code)
