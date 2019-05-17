#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import ast

#set constants
angle_min= -1.57079637051
angle_max= 1.53938043118
angle_incr = 0.0314159281552

'''
TODO: this is simple just return the length of a given list.
'''
def get_length(scan_data):
	return len(scan_data)

'''
TODO: find the index of the closest point in the scan_data
'''
def get_index_of_closest_point(scan_data):
        for j in range(0,len(scan_data)):
               if scan_data[j] >0:
                       break
        for i in range(0,len(scan_data)):
               if (scan_data[i] < scan_data[j]) and (scan_data[i] != 0):
                       j=i
	return j

'''
TODO: calculate the angle in rad for the closest point in scan_data
'''
def get_angle_of_closest_point(scan_data):
        close_point = get_index_of_closest_point(scan_data)
        angle_inc = (close_point)*angle_incr + angle_min
        return angle_inc


def get_laserdata(path):
	file = open(path, "r")

	laserdata_raw = file.read()
	laserdata = ast.literal_eval(laserdata_raw)

	return laserdata


if __name__ == "__main__":

	#what is wrong with the print statement below? The print should look like this in your console:
	'''
	####################
	Python exercise
	####################
	'''
	print (20*"#"+"\nPython exercise\n"+20*"#")

	#read raw laser data
	scan_data = get_laserdata("laser-testdata/laser-testdata_1")

	#print length of scan_data
	print("Lenght of scan data: {0}".format(get_length(scan_data)))

	#print index of closest point
	print("Index of closest point: {0}".format(get_index_of_closest_point(scan_data)))

	#print angle of closest point
	print("Angle of closest point: {0}".format(get_angle_of_closest_point(scan_data)))
