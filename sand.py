import random

class Grain:
	h = 0
	r = 0
	a = 0
	level = 0

class Pile:
	def addGrainAtRandom(self, range):

	def destabilizedBy(self, g):
		if(g.h > 1)
			return True

	def beginAvalanche(self, g):
		if random.getrandbits(1):
			self.downright(g)
		else:
			self.downleft(g)

def main():
	for i in range(0, 1000):
		g = pile.addGrainAtRandom(range)
		if pile.destabilizedBy(g):
			pile.beginAvalanche(g)