# utility class for handling buttons


class Button:
	# this will handle locations
	x_offset = 0
	y_offset = 0
	width = 0
	height = 0

	def __init__(self, x_offset=0, y_offset=0, width=0, height=0):
		self.x_offset = x_offset
		self.y_offset = y_offset
		self.width = width
		self.height = height

	def is_cursor_inside(self, cursor):
		return self.x_offset <= cursor[0] <= self.x_offset + self.width and \
			self.y_offset <= cursor[1] <= self.y_offset + self.height
