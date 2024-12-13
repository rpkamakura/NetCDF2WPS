import numpy as np
import pywinter.winter as pyw

infile = './data/SST:2021-10-25_12'

interfile = pyw.rinter(infile)

print(interfile.keys())
print(interfile['SST'].general)
print(interfile['SST'].geoinfo)
