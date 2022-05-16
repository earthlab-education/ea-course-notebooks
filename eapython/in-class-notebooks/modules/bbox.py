"""
A Bounding Box class

copyright
authors
"""

import geopandas as gpd
from shapely.geometry import Point

class BBox:
	"""
	Corner coordinates of a bounding box
	"""
	
	def __init__(self, minx, miny, maxx, maxy, crs='EPSG:4326'):
		if minx > 180:
			raise ValueError('x values cannot exceed 180')
			
		self.minx = minx if (minx < maxx) else maxx
		self.miny = miny
		self.maxx = maxx if (minx < maxx) else minx
		self.maxy = maxy
		self.crs = crs
		
	@property
	def min_lon(self):
		return self.minx
	
	@property
	def _min_point(self):
		return Point(self.minx, self.miny)
	
	@property
	def _max_point(self):
		return Point(self.maxx, self.maxy)
	
	@property
	def _gdf(self):
		return gpd.GeoDataFrame(
			{'geometry': [self._min_point, self._max_point]},
			crs=self.crs)
	
	def to_crs(self, crs):
		gdf_reproj = self._gdf.to_crs(crs)
		self.minx = gdf_reproj.loc[0].geometry.x
		self.miny = gdf_reproj.loc[0].geometry.y
		self.maxx = gdf_reproj.loc[1].geometry.x
		self.maxy = gdf_reproj.loc[1].geometry.y

		