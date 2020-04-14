INSTANCE_ID = 'your ID from sentinel hub'  # In case you put instance ID into configuration file you can leave this unchanged

%reload_ext autoreload
%autoreload 2
%matplotlib inline
import datetime
import numpy as np

import matplotlib.pyplot as plt
from sentinelhub import WmsRequest, WcsRequest, MimeType, CRS, BBox
def plot_image(image, factor=1):
    """
    Utility function for plotting RGB images.
    """
    fig = plt.subplots(nrows=1, ncols=1, figsize=(15, 7))

    if np.issubdtype(image.dtype, np.floating):
        plt.imshow(np.minimum(image * factor, 1))
    else:
        plt.imshow(image)

from sentinelhub import CustomUrlParam


# Tip: if you want to insert the coordinates from google, you will need to set
# the first two coordinates for the upper left corner (-122.41, 39.31)
# and second two (-122.75, 39.55) will refer to lower right corner of the box
# Lastly: lat long from Google maps needs to be switched around (e.g. for lower corner 
# google maps will give you '39.55, -122.75'; you need to switch out around to read -122.75, 39.55)

betsiboka_coords_wgs84 = [-122.41, 39.31, -122.75, 39.55]
betsiboka_bbox2 = BBox(bbox=betsiboka_coords_wgs84, crs=CRS.WGS84)


my_url = 'https://raw.githubusercontent.com/sentinel-hub/custom-scripts/master/sentinel-2/markuse_fire/script.js'

evalscripturl_wms_request = WmsRequest(layer='TRUE-COLOR-S2-L1C', # Layer parameter can be any existing layer
                                       bbox=betsiboka_bbox2,
                                       time='2018-08-28',
                                       width=512,
                                       instance_id=INSTANCE_ID,
                                       custom_url_params={CustomUrlParam.EVALSCRIPTURL: my_url})

evalscripturl_wms_data = evalscripturl_wms_request.get_data()
plot_image(evalscripturl_wms_data[0])
