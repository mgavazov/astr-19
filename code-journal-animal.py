#This program will declare a class 
#That describes my favorite animal

import sys

class Shape:

	def print(self):
		print("My favorite animal is my cat SASHO")
		print(f"Length of arms = {self.arm_length}")
		print(f"Length of legs = {self.leg_length}")
		print(f"Number of eyes = {self.num_eyes}")
		print(f"Does it have a tail? = {self.tail}")
		print(f"Is it furry? = {self.furry}")

	def __init__(self,alenght=7,llenght=7,neyes=2,tail=True,furry=True):
		self.arm_length  = alenght
		self.leg_length  = llenght
		self.num_eyes    = neyes
		self.tail        = tail
		self.furry       = furry

def main():

	#number of length and eyes
	alenght = float(7.0)
	llenght = float(7.0)
	neyes   = 2

	#If its furry and has a tail
	tail = True
	furry = True

	our_shape = Shape(alenght=alenght,llenght=llenght,neyes=neyes,tail=True,furry=True)

	our_shape.print()

if __name__ == '__main__':
	main()