# import laspy.file
# import laspy.header

import rasterio as rio
from rasterio.warp import transform
from rasterio.crs import CRS
import subprocess
import json
import sys
import logging


LOG_FORMAT = '[%(levelname)s] %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=LOG_FORMAT)



def pc2dsm(file_path, grid_size, horizontal_srs_wkt, WORKING_DIR):

	# get the crs from the las file
	# the same crs will be used for the output raster
	# crs_las = {'init': 'EPSG:3945'}
	crs_las = CRS.from_string(horizontal_srs_wkt)

	pipeline_max = [
		file_path,
		{
			"type":"writers.gdal",
			"filename":str(WORKING_DIR/"max.tif"),
			"output_type":"max",
			"gdaldriver":"GTiff",
			"window_size":3,
			"resolution":grid_size
		}
	]

	with open(WORKING_DIR / 'pipeline_max.json', 'w') as outfile:
		json.dump(pipeline_max, outfile)

	logging.debug('Generating max rasters...')
	#generate rasters: max (description of pipelines in .json files)
	subprocess.run('pdal pipeline '+str(WORKING_DIR/'pipeline_max.json'), shell=True)


	logging.debug('adding a crs to the raster...')

	dataset_max = rio.open(WORKING_DIR/'max.tif')

	new_dataset = rio.open(WORKING_DIR/'output.tif', 'w',
									driver = dataset_max.driver,
									nodata = dataset_max.nodata,
									height=dataset_max.height, width=dataset_max.width,
									count=dataset_max.count, dtype=rio.float64,
									crs=crs_las, transform=dataset_max.transform)

	band_max = dataset_max.read(1)

	new_dataset.write(band_max, 1)

	logging.debug('All done')


if __name__ == "__main__":

	pc2ph('input.las', 0.2)