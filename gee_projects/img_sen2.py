# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/satellite_data/sentinel_2.ipynb.

# %% auto 0
__all__ = ['access_s2_image']

# %% ../nbs/satellite_data/sentinel_2.ipynb 3
import geopandas as gpd
import seaborn as sns
from shapely.geometry import Point
import json
import ee

ee.Authenticate()
ee.Initialize(project='ee-reutkeller')

from . import util_func as utils

# %% ../nbs/satellite_data/sentinel_2.ipynb 5
class access_s2_image():
  
  def __init__(self,
               path_to_geometry : str , # path to geometry file, can be .shp or .gpkg . example : r"D:\git\gee_maps\nbs\geometry\test_bbox.gpkg"
               crs : str , #coordinate reference system to work with
               ):
    self.crs = crs
    self.gdf = utils.read_gdf(geometry_path=path_to_geometry,crs=self.crs)

    