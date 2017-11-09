import gspread
import pandas 
from oauth2client.service_account import ServiceAccountCredentials
#import numpy
#import math

# create client to interact with the GDrive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(creds)

# read worksheets from workbook
workbook = gc.open("hmp_mars")
nodes = workbook.get_worksheet(0)
images = workbook.get_worksheet(1)
filtered = workbook.get_worksheet(2)

# test what worksheets look like
#print(nodes.row_count)
#print(images.row_count)

# create dataframes from worksheets
nodes_df = pandas.DataFrame(nodes.get_all_records())
images_df = pandas.DataFrame(images.get_all_records())
filtered_df = pandas.DataFrame(filtered.get_all_records()) 

# test what the dataframes look like
#print(nodes_df)
#print(images_df)

# create distance function ... or not
#def distance_calculator()

"""
def node_range(start,end,step):
    while start <= end:
        yield start
        start += step

def images_range(start,end,step):
    while start <= end:
        yield start
        start += step
"""

for node_index in xrange(0,5476):
	d_min = 35
	print "node: ", node_index
	for image_index in xrange(0,8111):
		print "image: ", image_index
		xnode = nodes_df.get_value(node_index,'xnode')
		ximage = images_df.get_value(image_index,'ximage')
		ynode = nodes_df.get_value(node_index,'ynode')
		yimage = images_df.get_value(image_index,'yimage')
		#d = math.sqrt(numpy.square(xnode-ximage)+numpy.square(ynode-yimage))
		d = (((xnode-ximage)**2)+((ynode-yimage)**2))**0.5
		#print "node: ", node_index
		#print "image: ", image_index
		#print "distance: ", d
		print "distance: ", d
		if d < d_min:
			d_min = d
			chosen_image = images_df.get_value(image_index,'image_id')
			filtered_df.ix[node_index,'node_index'] = node_index
			filtered_df.ix[node_index,'nearest_image'] = chosen_image
			filtered_df.ix[node_index,'distance'] = d_min
			#nodes_df.ix[node_index,'nearest_image'] = chosen_image
			print "chosen image: ", chosen_image
			print "MINIMUM DISTANCE: ", d_min
			#print "chosen image: ", chosen_image
			#print "MINIMUM DISTANCE: ", d_min
	
"""
for index, row in nodes_df.iterrows():
	for index, row in images_df.iterrows():
		xnode = row['xnode']
		ximage = row['ximage']
		ynode = row['ynode']
		yimage = row['yimage']
		d_min = 1000
		d = math.sqrt(numpy.square(xnode-ximage)+numpy.square(ynode-yimage))
		print(d_min)
		print(d) 
		if d < d_min:
			d = d_min
			chosen_image = images_df.get_value(index,'image_id')
			nodes_df.ix[index,'nearest_image'] = chosen_image
"""
"""
for row in nodes_df:
	for row in images_df:
		xnode = nodes_df.get_value(row,'xnode')
		ximage = images_df.get_value(row,'ximage')
		ynode = nodes_df.get_value(row,'ynode')
		yimage = images_df.get_value(row,'yimage')
		d_min = 1000
		d = math.sqrt(numpy.square(xnode-ximage)+numpy.square(ynode-yimage))
		print(d_min)
		print(d) 
		if d < d_min:
			d = d_min
			chosen_image = images_df.get_value(row,'image_id')
			nodes_df.ix[row,'nearest_image'] = chosen_image
"""

filename = 'filtered_images.csv'
filtered_df.to_csv(filename, index=False, encoding='utf-8')