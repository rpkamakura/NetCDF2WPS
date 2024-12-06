import numpy as np
import pywinter.winter as pyw

infile = './data/FILE:2021-10-25_12'

interfile = pyw.rinter(infile)

print(interfile.keys())
print(interfile['TT2M'].general)
print(interfile['TT2M'].geoinfo)