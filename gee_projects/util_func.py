# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/utilities/utilities.ipynb.

# %% auto 0
__all__ = ['read_gdf', 'gdf_to_featureCollection', 'list_dates', 'find_closest_date', 'get_day_before_day_after',
           'get_reducer_with_names', 'reduce_region']

# %% ../nbs/utilities/utilities.ipynb 3
import geopandas as gpd
import seaborn as sns
from shapely.geometry import Point
import json
import ee
from datetime import datetime, timedelta
import geemap 

ee.Authenticate()
ee.Initialize(project='ee-reutkeller')

from . import const_vars as const
from . import img_sen2 as sen2
from . import util_func as utils

# %% ../nbs/utilities/utilities.ipynb 5
def read_gdf(geometry_path : str , #path to geometry file (.shp /.gpkg). Path string should be written with r, for example r"path/to/geom/geom.gpkg"
                  crs : str , #crs code , for example '4326'. the coordinate reference system code to be used
                  ):
  
  gdf = gpd.read_file(geometry_path)
  gdf = gdf.set_crs(crs)

  return gdf

# %% ../nbs/utilities/utilities.ipynb 8
def gdf_to_featureCollection(
  gdf : gpd.GeoDataFrame , # geopandas geodataframe data
  ):
  ''' convert geodataframe to ee FeatureCollection type, based on this post https://gis.stackexchange.com/questions/439924/convert-local-file-shp-csv-into-earth-engine-ee-object'''
  
  # convert to json
  geo_json = gdf.to_json()

  #convert to FeatureCollection
  featureCollection = ee.FeatureCollection(json.loads(geo_json))


  return featureCollection
  

# %% ../nbs/utilities/utilities.ipynb 11
def list_dates(img_coll):
  # Function to extract dates from image collection
  def extract_dates(img):
      date = ee.Date(img.get(const.system_time_start_str)).format(const.date_format_1)
      return ee.Feature(None, {'date': date})

  # Map the function over the image collection
  dates_list = img_coll.map(extract_dates).aggregate_array('date').getInfo()
  return dates_list



# %% ../nbs/utilities/utilities.ipynb 12
def find_closest_date(user_date : str , # the date that the user wants to get image for
                      date_list : list , #list of available dates in imageCollection
                      ):
    '''
The function identifies the nearest date in the image collection based on the provided reference date'''

    # Convert user-provided date string to datetime object
    user_datetime = datetime.strptime(user_date, const.date_format_2)

    # Convert the list of date strings to datetime objects
    date_objects = [datetime.strptime(date, const.date_format_2) for date in date_list]

    # Find the closest date in the list
    closest_date = min(date_objects, key=lambda date: abs(date - user_datetime))

    # Convert the closest date back to string format
    closest_date_str = closest_date.strftime(const.date_format_2)

    return closest_date_str

# %% ../nbs/utilities/utilities.ipynb 13
def get_day_before_day_after(
        date_str : str , # Produce list with the date before and the date after a given date
                             ):
        input_date = datetime.strptime(date_str, const.date_format_2)
        day_before = (input_date - timedelta(days=1)).strftime(const.date_format_2)
        day_after = (input_date + timedelta(days=1)).strftime(const.date_format_2)
        return [day_before, day_after]

# %% ../nbs/utilities/utilities.ipynb 15
def get_reducer_with_names( reducer : str , # the reducer to be used, one of the following : mean, median, min, max,std, mode
                           ):
  if reducer == 'mean':
    ee_reducer = ee.Reducer.mean()

  elif reducer == 'median':
    ee_reducer = ee.Reducer.median()

  elif reducer == 'min':
    ee_reducer = ee.Reducer.min()

  elif reducer == 'max' :
    ee_reducer == ee.Reducer.max()

  elif reducer == 'mode':
    ee_reducer == ee.Reducer.mode()

  elif reducer == 'std':
    ee_reducer == ee.Reducer.stdDev()

  return reducer, ee_reducer 

# %% ../nbs/utilities/utilities.ipynb 16
# function to calculate the mean spectral index for the region of interest (polygon)
def reduce_region(img : ee.Image , # the image that we want to apply the statistics calculation on
                  reducer :  str , #the reducer to be used, should be imported from constant module.       
                  fc : ee.featurecollection , #featureCollection , the geometry that will be used to sample the region
                  scale : float , # the scale of the sampled image
                  
                  ):
    _, ee_reducer  = get_reducer_with_names(reducer)

    reduced_regions = img.reduceRegion(
        reducer=ee_reducer,
        geometry=fc,
        scale=scale,  
        maxPixels= const.max_pixels_float
    )

    return geemap.ee_to_gdf(reduced_regions, selectors=None, verbose=False)
    # return img.set('date', img.date().format('YYYY-MM-dd')).set(reducer,reduced_region.get('NDVI'))

