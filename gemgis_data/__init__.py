"""Top-level package for GemGIS Data."""

__title__ = 'GemPy Geographic - GemGIS: Spatial Data processing for geomodeling'

__abstract__ = """We attempt to simplify the access to open-source spatial data processing for geological modeling with 
the development of **GemGIS, a Python-based open-source library**.GemGIS wraps and extends the functionality of 
packages known to the geo-community such as [GeoPandas](https://geopandas.org/), 
[rasterio](https://rasterio.readthedocs.io/en/latest/#), [OWSLib](https://geopython.github.io/OWSLib/), 
[Shapely](https://shapely.readthedocs.io/en/latest/manual.html), [PyGEOS](https://pygeos.readthedocs.io/en/latest/), 
[PyVista](https://docs.pyvista.org/), [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) and the 
geomodelling package [GemPy](https://docs.gempy.org/). The aim of GemGIS, as indicated by the name, is to become a 
bridge between conventional geoinformation systems (GIS) such as ArcGIS and QGIS, and geomodelling tools such as GemPy,
allowing simpler and more automated workflows from one environment to the other."""

__authors__ = """Alexander Jüstel, Miguel de la Varga, Nils Chudalla, Stefan Back, Florian Wellmann"""

__correspondence_email__ = 'alexander.juestel@rwth-aachen.de'

__affiliations__ = 'CGRE - RWTH Aachen University'

__version_date__ = '2022-12-30'

__version__ = '0.0.2'

__changelog__ = """What is new in version 0.0.2:

- Minor bug fixes

"""



from gemgis_data.gemgis_data import *
