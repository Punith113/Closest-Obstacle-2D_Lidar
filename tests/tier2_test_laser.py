#!/usr/bin/env python#
# -*- coding: utf-8 -*-
import pytest
import tier2_main


scan = (tier2_main.get_laserdata("laser-testdata/laser-testdata_1"))
	
def test_index_of_nearest_point():	
	assert tier2_main.get_index_of_closest_point(scan) == 5

def test_angle_of_nearest_point():
	
	angle = tier2_main.get_angle_of_closest_point(scan)
	anglegoal = -1.413716729734
	
	assert abs(angle-anglegoal) < 0.01
