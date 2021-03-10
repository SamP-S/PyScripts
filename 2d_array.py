from random import random

##---Functions---##

# Random char to fill grid
def GetChar():
	r = round(random())
	if r == 0:
		return "#"

# Initialise
def GetGrid(width, height):
	tmp = [[0 for i in range(width)] for j in range(height)]
	for y in range(height):
		for x in range(width):
			tmp[y][x] = y * width + x
	return tmp

# Draw
def DrawGrid(tmp):
	print
	for row in tmp:
		print(row)
	print

##---Main---##

print("python script")

grid = GetGrid(4, 4)
DrawGrid(grid)

