import pytest
from rng import MersenneTwister


class TestMersenneTwister:

	
	def test_seeding(self):
		mt = MersenneTwister(0)
		r1 = mt.get()
		
		mt = MersenneTwister(0)
		r2 = mt.get()
		
		assert r1 == r2
		
