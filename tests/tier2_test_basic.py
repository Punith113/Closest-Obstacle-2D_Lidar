#!/usr/bin/env python#
# -*- coding: utf-8 -*-
import pytest
import tier2_main

	
def test_readLaserdata():
	assert tier2_main.get_length(tier2_main.get_laserdata("laser-testdata/laser-testdata_1")) == 99
	
