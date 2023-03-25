
class MersenneTwister:
	
	(w, n, m, r) = (32, 624, 397, 31)
	a = 0x9908B0DF
	(u, d) = (11, 0xFFFFFFFF)
	(s, b) = (7, 0x9D2C5680)
	(t, c) = (15, 0xEFC60000)
	l = 18
	f = 1812433253

	def __init__(self, seed: int):
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
		
	def get(self):
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
		return (y & 0xFFFFFFFF) / (2 ** self.w - 1)
	
	def _twist(self):
		for i in range(self.n):
			x = (self._arr[i] & self._upper_mask) + \
				(self._arr[(i+1) % self.n] & self._lower_mask)
			xA = x >> 1
			if (x % 2) != 0:
				xA = xA ^ self.a
			self._arr[i] = self._arr[(i+self.m)% self.n] ^ xA
		self._index = 0
	

if __name__ == '__main__':
	rng = MersenneTwister(1)
	for _ in range(10):
		print(rng.get())
