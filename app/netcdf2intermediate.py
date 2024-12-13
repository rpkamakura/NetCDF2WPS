import numpy as np
from netCDF4 import Dataset
import pywinter.winter as pyw

#dt_input = input("Please type the path to the dataset: ")
#dataset = Dataset(dt_input, 'r')
dataset = Dataset('./data/20211025120000-UKMO-L4_GHRSST-SSTfnd-OSTIA-GLOB_REP-v02.0-fv02.0.nc', 'r')

print(dataset.variables.keys())
dataset
lat = dataset.variables['lat'][:]
lon = dataset.variables['lon'][:]

dlat = dataset.geospatial_lat_resolution
dlon = dataset.geospatial_lon_resolution

sst = dataset.variables['analysed_sst'][:].data[0]

winter_geo = pyw.Geo0(lat[0], lon[0], dlat, dlon)
winter_t2m = pyw.V2d('SST', sst)

total_fields = [
    winter_t2m,
]

pyw.cinter('SST', '2021-10-25_12', winter_geo, total_fields, './data/')
