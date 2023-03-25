import pytest
from rng import MersenneTwister


class TestMersenneTwister:

	
	def test_seeding(self):
		for i in range(100):
			mt = MersenneTwister(i)
			r1 = mt.random()
		
			mt = MersenneTwister(i)
			r2 = mt.random()
		
			assert r1 == r2

	def test_randint_err(self):
		mt = MersenneTwister()
		with pytest.raises(ValueError):
			mt.randint(low=2, high=1)
		with pytest.raises(ValueError):
			mt.randint(low=1, high=1)

	def test_randint(self):
		mt = MersenneTwister()
		l = []
		for _ in range(1000):
			r = mt.randint(low=1, high=6)
			assert 1 <= r <= 6
			l.append(r)
		s = set(l)
		for i in range(1,7):
			assert i in s

	def test_randint_offset(self):
		mt = MersenneTwister()
		l = []
		for _ in range(1000):
			r = mt.randint(low=990, high=1000)
			assert 990 <= r <= 1000
			l.append(r)
		s = set(l)
		for i in range(990,1001):
			assert i in s

		
