from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import csv
import netCDF4


#load x and y data from netCDF file
ncFile = netCDF4.Dataset('../Model Combined/o3_surface_20180701000000.nc')
x = ncFile.variables['lat'][:-2]
y = ncFile.variables['lon'][:-2]
#read z data from csv file
data = np.genfromtxt('24hour/24HR_Orig_01.csv',delimiter = ',')
data = np.array(data)
data = np.transpose(data,(1,0))


xx, yy = np.meshgrid(x, y)
# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# resolution = 'c' means use crude resolution coastlines.
#m = Basemap(projection='mill',llcrnrlat=25,urcrnrlat=75,llcrnrlon=-35,urcrnrlon=30,resolution='c')
m = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c')
m.drawcoastlines()
x,y = m(yy,xx)
plt.contourf(x,y,data,10)
plt.colorbar()
#plt.scatter(x,y)
plt.title("Data visualization")
plt.show()
