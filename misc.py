#Read sabple data

import csv
from pygeocoder import Geocoder


# open samle data with per row dictionary
data = csv.DictReader(open("sampledata.csv"))

# GeoCode from address
latlon = []
propvalue = []
for row in data:
    propvalue.append(row["VALACT"])
    addr = [row["PRPSTRNUM"], row["PRPSTRDIR"], row["PRPSTRNAM"], row["PRPSTRTYP"], row["PRPSTRSFX"], 
            row["PRPSTRUNT"], row["PRPCTYNAM"], row["PRPSTENAM"], row["PRPZIP5"]]
    addr = ' '.join(addr)
    results = Geocoder.geocode(addr)
    latlon.append(results[0].coordinates)

# for coor in latlon:
#     print(coor)
# for val in propvalue:
#     print(val)

#########################

import scipy.sparse.sparsetools
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

points = numpy.asarray(latlon)

tri = Delaunay(points)

plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.show()

#########################
# Fails
#########################
from matplotlib.tri import Triangulation, UniformTriRefiner, CubicTriInterpolator
import numpy

propvalue = numpy.asarray(propvalue)
x = 100*points[:,0]
y = 100*points[:,1]
triang = Triangulation(x, y)

tci = CubicTriInterpolator(triang, propvalue)
(Ex, Ey) = tci.gradient(triang.x, triang.y)
E_norm = np.sqrt(Ex**2 + Ey**2)
