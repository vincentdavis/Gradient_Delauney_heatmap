Gradient_Delauney_heatmap
========================

Using property values calculates gradient based on a Delauney triangulation

Referance code is in the /ref folder

/ref/trigradient_demo.py : 
    This example is a good referance for taking a set of points with location and value(calculated) 
    and constricting a Delauney triagulation and then calculated gradiant. The plot is not quite what we want.
    
/ref/tricontour_vs_griddata.py:
    Comparison of griddata and tricontour for an unstructured triangular grid.
                      
 Jeff Kaufman has some great maps using rent data. Visualy this is what I want.
      Here are some examples http://rentheatmap.com/
      Code here https://github.com/jeffkaufman/apartment_prices
      He uses his own K nearest algorythm, scipy has an implimentation here
      http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.cKDTree.html#scipy.spatial.cKDTree
      
Useful Scipy page  http://docs.scipy.org/doc/scipy/reference/spatial.html


For geocoding:
    pygeocoder seems to work well http://code.xster.net/pygeocoder/wiki/Home it uses the google api.
    geopy Have not tried.  https://code.google.com/p/geopy/wiki/GettingStarted
    

  
