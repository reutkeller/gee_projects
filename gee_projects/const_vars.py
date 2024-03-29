# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/utilities/CONSTANTS.ipynb.

# %% auto 0
__all__ = ['CLOUD_FILTER', 'CLD_PRB_THRESH', 'NIR_DRK_THRESH', 'CLD_PRJ_DIST', 'BUFFER', 'CLOUDY_PIXEL_PERCENTAGE_STR',
           'COPERNICUS_S2_CLOUD_PROBABILITY_STR', 's2_img_collection_str', 's2cloudless_str', 'probability_str',
           'clouds_name_bands_str', 'SCL_str', 'SCL_VALUE_int', 'SR_BAND_SCALE_int', 'B8_str', 'dark_pixels_str',
           'direction_int', 'MEAN_SOLAR_AZIMUTH_ANGLE_str', 'int_10', 'cloud_transform_str', 'distance_str',
           'scale_str', 'scale_str_size', 'shadows_str', 'crs_str', 'scale_2_int', 'cloudmask_str', 'find_band_str',
           'system_time_start_str', 'date_format_1', 'date_format_2', 'date_str', 'MEAN_reducer', 'MEDIAN_reducer',
           'MAX_reducer', 'MIN_reducer', 'MODE_reducer', 'max_pixels_float', 'get_reducer_with_names']

# %% ../nbs/utilities/CONSTANTS.ipynb 3
import geopandas as gpd
import seaborn as sns
import ee
import geemap 
ee.Authenticate()
ee.Initialize(project='ee-reutkeller')


# %% ../nbs/utilities/CONSTANTS.ipynb 5
CLOUD_FILTER = 60
CLD_PRB_THRESH = 50
NIR_DRK_THRESH = 0.15
CLD_PRJ_DIST = 1
BUFFER = 50

CLOUDY_PIXEL_PERCENTAGE_STR='CLOUDY_PIXEL_PERCENTAGE'
COPERNICUS_S2_CLOUD_PROBABILITY_STR='COPERNICUS/S2_CLOUD_PROBABILITY'

# %% ../nbs/utilities/CONSTANTS.ipynb 6
#S2 image collection
s2_img_collection_str='COPERNICUS/S2_SR_HARMONIZED'

#clouds bands names
s2cloudless_str='s2cloudless'
probability_str='probability'
clouds_name_bands_str='clouds'


#shadow bands names
SCL_str= 'SCL'
SCL_VALUE_int = 6
SR_BAND_SCALE_int = 1e4
B8_str = 'B8'
dark_pixels_str='dark_pixels'
direction_int = 90
MEAN_SOLAR_AZIMUTH_ANGLE_str='MEAN_SOLAR_AZIMUTH_ANGLE'
int_10 = 10
cloud_transform_str='cloud_transform'
distance_str = 'distance'
scale_str= 'scale'
scale_str_size = 100
shadows_str = 'shadows'
crs_str = 'crs'
scale_2_int = 20
cloudmask_str ='cloudmask'
find_band_str = 'B.*'


# %% ../nbs/utilities/CONSTANTS.ipynb 8
system_time_start_str ='system:time_start'
date_format_1 = 'YYYY-MM-dd'
date_format_2 = '%Y-%m-%d'
date_str='date'

# %% ../nbs/utilities/CONSTANTS.ipynb 9
def get_reducer_with_names( reducer : str ):
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

  return reducer, ee_reducer 







MEAN_reducer = ee.Reducer.mean()
MEDIAN_reducer = ee.Reducer.median()
MAX_reducer = ee.Reducer.max()
MIN_reducer = ee.Reducer.min()
MODE_reducer = ee.Reducer.mode()



max_pixels_float = 1e13
