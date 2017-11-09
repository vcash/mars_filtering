# mars_filtering

A quick and dirty (super inefficient) program that: 
1. Connects to a Google Sheet that contains the x,y,z coordinates of images as well as the x,y,z coordinates of the nodes of an arbitrary grid using Google APIs
2. Calculates the z-plane (x,y) distance from _each_ node of _each_ image and filters the image with the minimum distance
3. Returns a .csv with all the filtered images' file names
