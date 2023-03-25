import pytest
from rng import MersenneTwister


class TestMersenneTwister:

	
	def test_seeding(self):
		for i in range(100):
			mt = MersenneTwister(i)
			r1 = mt.get()
		
			mt = MersenneTwister(i)
			r2 = mt.get()
		
			assert r1 == r2
		
