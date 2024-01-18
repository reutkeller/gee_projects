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
from . import const_vars as const
from . import mask_s2 as mask_s2

# %% ../nbs/satellite_data/sentinel_2.ipynb 5
class access_s2_image():
  
  def __init__(self,
               path_to_geometry : str , # path to geometry file, can be .shp or .gpkg . example : r"D:\git\gee_maps\nbs\geometry\test_bbox.gpkg"
               crs : str , #coordinate reference system to work with
               start_date : str , # Start date for searching images. , 
               end_date : str , # End date for searching images.
               ):
    
    self.crs = crs
    self.fc = utils.gdf_to_featureCollection(
      utils.read_gdf(geometry_path=path_to_geometry,crs=self.crs))
    self.start_date=start_date
    self.end_date=end_date
    
    
    self.fc = utils.gdf_to_featureCollection(utils.read_gdf
                                        (geometry_path=path_to_geometry,crs=self.crs))
    
    s2_sr_cld_col_eval = mask_s2.get_s2_sr_cld_col(self.fc, self.start_date, self.end_date)




    

    
