import time
from math import ceil
from typing import Optional


class MersenneTwister:
	
	(w, n, m, r) = (32, 624, 397, 31)
	a = 0x9908B0DF
	(u, d) = (11, 0xFFFFFFFF)
	(s, b) = (7, 0x9D2C5680)
	(t, c) = (15, 0xEFC60000)
	l = 18
	f = 1812433253

	def __init__(self, seed: Optional[int] = None):
		"""Init a Mersenne-Twister type random number generator.

		Parameters
		----------

		seed: Optional[int], default=None
			The seed of the RNG. If None then use unix-timestamp to seed generator.
		"""
		if seed is None:
			seed = ceil(time.time())
		self._seed = seed
		arr = [0 for i in range(self.n)]
		arr[0] = seed
		for i in range(1, self.n):
			tmp = self.f * (arr[i-1] ^ (arr[i-1] >> (self.w-2) )) + 1
			arr[i] = tmp & 0xFFFFFFFF
		self._arr = arr
		self._index = self.n
		self._lower_mask = (1 << self.r) - 1
		self._upper_mask = ~self._lower_mask & 0xFFFFFFFF
		
	def random(self) -> float:
		"""Generate a random float in range [0,1].
		
		Return
		------

		r: int
			A random float in range [0, 1].
		"""
		if self._index >= self.n:
			if self._index > self.n:
				raise ValueError("Generator was never seeded")
			self._twist()
		y = self._arr[self._index]
		y = y ^ ((y >> self.u) & self.d)
		y = y ^ ((y << self.s) & self.b)
		y = y ^ ((y << self.t) & self.c)
		y = y ^ (y >> 1)

		self._index += 1
		# Normalize to range [0, 1] since default is integer in range [0, 2^w - 1].
		return (y & 0xFFFFFFFF) / (2 ** self.w - 1)

	def randint(self, *, low: int, high: int) -> int:
		"""Generate a random integer in range [low, high] (both endpoints included).

		Parameters
		----------

		low: int
			The lower point in range (inclusive).
		high: int
			The upper point in range (inclusive).


		Return
		------

		r: int
			A random integer in range [low, high].
		"""
		if low >= high:
			raise ValueError(f"Low should be strictly lower than high. Got {low=} and {high=}")
		r = ceil(self.random() * (high - low+1)) + low -1
		return r
	
	def _twist(self):
		for i in range(self.n):
			x = (self._arr[i] & self._upper_mask) + \
				(self._arr[(i+1) % self.n] & self._lower_mask)
			xA = x >> 1
			if (x % 2) != 0:
				xA = xA ^ self.a
			self._arr[i] = self._arr[(i+self.m)% self.n] ^ xA
		self._index = 0
	