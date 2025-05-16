# core data types
a = 3		# integer
b = 3.14	# float/double
c = "pi"	# string
d = True	# boolean

# core data structures
x = [1, 2, 3] 	# list
y = {"name": "John", "age": 30}	# dictionary

# basic get array functions
def Get_1D_Array(size):
	return [None for i in range(size)]

def Get_ND_Array(n, size):
	if n == 0:
		return None
	return [Get_ND_Array(n-1, size) for i in range(size)]

# basic tree structure with parent - child relationships

class tree_node:

	def __init__(self, data=None, parent=None):
		self.root = False
		self.data = data
		self.parent = parent
		self.children = []

		if parent == None:
			self.root = True
		else:
			parent.children.append(self)

	# can just print(tree_node) for printing
	def __repr__(self):
		self.print()
		return ""

	# printing function
	def print(self, padding=" "):
		print(padding + self.data)
		for child in self.children:
			child.print(padding + " ")
