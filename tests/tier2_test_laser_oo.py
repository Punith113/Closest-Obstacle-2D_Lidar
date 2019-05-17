#!/usr/bin/env python#
# -*- coding: utf-8 -*-

import tier2_main_class as tier2_class
import math

class Test:

	def setup(self):
		self.app = tier2_class.LaserModel(-math.pi/2, math.pi/2, 2.0, 30.0)
		self.app.update_laserdata("laser-testdata/laser-testdata_2")
		self.app.set_angle_inc(self.app.calc_angle_inc())
		#self.app.laser_read_cycle = 0

	def test_index_of_nearest_point(self):
		results = [7,252,233,213,209,205,209,7]

	 	for i,k in enumerate(results):

			self.app.update_laserdata("laser-testdata/laser-testdata_2")
			assert self.app.laser_read_cycle == i+1
			assert self.app.calc_index_of_closest_point() == k

	def test_angle_of_nearest_point(self):

		results = [-1.50953964553,0.634444198845,0.468176063975,0.293156974639,0.258153156771,0.223149338904,0.258153156771]

	 	for i,k in enumerate(results):

			self.app.update_laserdata("laser-testdata/laser-testdata_2")
			assert self.app.laser_read_cycle == i+1
			assert abs(self.app.calc_angle_of_closest_point()-k) < 0.01

	def test_angle_inc(self):

			assert abs(self.app.angle_inc-0.00875095446682) < 0.0001
