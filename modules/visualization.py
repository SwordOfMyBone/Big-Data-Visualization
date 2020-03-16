from mpl_toolkits.basemap import Basemap
import numpy as np

def createContMap(x,y,z,zVarName):
    xx, yy = np.meshgrid(x,y)

    m = Basemap(projection='mill',llcrnrlat=min(y),urcrnrlat=max(y),\
               llcrnrlon=min(x),urcrnrlon=max(x),resolution='l', ax=ax1)

    #Convert to map projection cord.
    xx, yy = m(xx, yy)

    m.drawcoastlines()
    cont = m.contourf(xx, yy, data, 10,cmap = "inferno",alpha = 0.8)
    m.colorbar(cont, location = "bottom")


