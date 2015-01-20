# -*- coding: utf-8 -*-

def writeToFile(text, filename = "tmp.txt"):
    f = open(filename, 'a')
    f.write(text)
    f.write("\r\n")
    f.close