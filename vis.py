from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import netCDF4
import glob
from modules import calc



# load x (longitude) and y (latitude) data from combined model netCDF file.
ncFile = netCDF4.Dataset('./data/Model Combined/o3_surface_20180701000000.nc')
x = ncFile.variables['lon'][:-2]
y = ncFile.variables['lat'][:-2]
ncFile.close()

# read z data from csv files and calc mean for each data point.
pathList = glob.glob("./data/24Hour/24HR_CBE_*.csv") # Creates a list of paths using globbing.
data = calc.calcMean(pathList)  

# Creates a meshgrid with the same dimensions as the data so that it can be plotted.
xx, yy = np.meshgrid(x, y)

# Create two subplots
fig, (ax1, ax2) = plt.subplots(1,2)

# Create the Basemap using matplotlib. 
# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# resolution = 'c' means use crude resolution coastlines.
ax1.set_title("Cluster Based Ensemble Mean")
m = Basemap(projection='mill',llcrnrlat=31,urcrnrlat=70,\
            llcrnrlon=-25,urcrnrlon=45,resolution='l', ax=ax1)

#Convert to map projection cord.
xx, yy = m(xx, yy)
m.drawcoastlines()
cont = m.contourf(xx, yy, data, 10,cmap = "inferno",alpha = 0.8)
m.colorbar(cont, location = "bottom")



#setup other basemap
pathList = glob.glob("./data/24Hour/24HR_Orig_*.csv") 
data2 = calc.calcMean(pathList)  
m2 = Basemap(projection='mill',llcrnrlat=31,urcrnrlat=70,\
            llcrnrlon=-25,urcrnrlon=45,resolution='l', ax=ax2)
m2.drawcoastlines()
cont2 = m2.contourf(xx, yy, data2,10,cmap = "inferno",alpha = 0.8)
m2.colorbar(cont2, location = "bottom")
ax2.set_title("Original Dataset Mean over 24 Hours")

plt.tight_layout()
