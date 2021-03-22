from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
	Every command is a single character that takes up a line
	Any command that requires arguments must have those arguments in the second line.
	The commands are as follows:
		line: add a line to the edge matrix -
			takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
		ident: set the transform matrix to the identity matrix -
		scale: create a scale matrix,
				then multiply the transform matrix by the scale matrix -
				takes 3 arguments (sx, sy, sz)
		translate: create a translation matrix,
					then multiply the transform matrix by the translation matrix -
					takes 3 arguments (tx, ty, tz)
		rotate: create a rotation matrix,
				then multiply the transform matrix by the rotation matrix -
				takes 2 arguments (axis, theta) axis should be x y or z
		apply: apply the current transformation matrix to the edge matrix
		display: clear the screen, then
				draw the lines of the edge matrix to the screen
				display the screen
		save: clear the screen, then
			draw the lines of the edge matrix to the screen
			save the screen to a file -
			takes 1 argument (file name)
		quit: end parsing

See the file script for an example of the file format
"""

def get_args(actions, i, ints):
	args = actions[i].split()
	if ints:
		n_args = [int(x) for x in args]
		return n_args
	else:
		return args

def parse_file( fname, points, transform, screen, color ):
	f = open(fname, 'r')
	actions = f.read().split('\n')
	i = 0
	while( i < len(actions) ):
		a = actions[i].rstrip()
		
		if a == 'line':
			i+=1
			a = get_args(actions, i, True)
			add_edge(points, a[0], a[1], a[2], a[3], a[4], a[5])
		
		elif a == 'ident':
			ident(transform)
		
		elif a == 'scale':
			i+=1
			a = get_args(actions, i, True)
			s = make_scale(a[0], a[1], a[2])
			matrix_mult(s, transform)
		
		elif a == 'move':
			i+=1 
			a = get_args(actions, i, True)
			t = make_translate(a[0], a[1], a[2])
			matrix_mult(t, transform)
		
		elif a == 'rotate':
			i+=1
			a = get_args(actions, i, False)
			theta = float(a[1])
			if a[0] == 'x':
				r = make_rotX(theta)
			elif a[0] == 'y':
				r = make_rotY(theta)
			elif a[0] == 'z':
				r = make_rotZ(theta)
			matrix_mult(r, transform)
		
		elif a == 'apply':
			matrix_mult(transform, points)
		
		elif a == 'display':
			clear_screen(screen)
			draw_lines(points, screen, color)
			display(screen)

		elif a == 'save':
			i+=1
			a = get_args(actions, i, False)
			clear_screen(screen)
			draw_lines(points, screen, color)
			
			save_extension(screen, a[0])

		elif a == "quit":
			break

		else:
			break

		i+=1
