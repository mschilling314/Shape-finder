import common
import math #note, for this lab only, your are allowed to import math


def linspace(start, finish, entries):
    step = (finish - start)/entries
    res = []
    last = start
    for x in range(entries):
        res.append(last)
        last += step
    return res


class vars:
	radius = 30
	mspace = linspace(-10, 10, 2000)
	bspace = linspace(-1000, 1000, 2000)


def find_val(arr, val):
	for i in range(len(arr)):
		if math.isclose(arr[i], val):
			return i
	return -1


def argmax2d(arr):
	i = 0
	j = 0
	max = arr[0][0]
	for x in range(len(arr)):
		for y in range(len(arr[0])):
			if arr[x][y] > max:
				max = arr[x][y]
				i = x
				j = y
	return i, j


def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	line=common.Line()
	line.m=0
	line.b=0
	votes = common.init_space(2000, 2000)
	for x in range(common.constants.WIDTH):
		for y in range(common.constants.HEIGHT):
			if image[y][x] == 0:
				for m in range(2000):
					b = y - vars.mspace[m]*x
					bi = math.floor(b + 1000)
					if 0 <= bi and bi < 2000:
						votes[bi][m] += 1
	bi, mi = argmax2d(votes)
	line.m = vars.mspace[mi]
	line.b = vars.bspace[bi]
	return line


def dist(pt1, pt2):
	x = pt1[1] - pt2[1]
	y = pt1[0] - pt2[0]
	x = x * x
	y = y * y
	z = math.sqrt(x+y)
	return z


def pts_on_circle(y, x):
	pts = []
	ystart = max(0, y-vars.radius)
	yend = min(common.constants.HEIGHT, y+vars.radius)
	xstart = max(0, x-vars.radius)
	xend = min(common.constants.HEIGHT, x+vars.radius)
	for i in range(ystart, yend):
		for j in range(xstart, xend):
			rt = dist([x, y], [j, i])
			if math.isclose(vars.radius, rt):
				pts.append([i, j])
	return pts


def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	votes = common.init_space(200, 200)
	for y in range(len(image)):
		for x in range(len(image[0])):
			if image[y][x] == 0:
				pts = pts_on_circle(y, x)
				for pt in pts:
					votes[pt[0]][pt[1]] += 1
	circles = 0
	for v1 in range(200):
		for v2 in range(200):
			if votes[v1][v2] > 5:
				circles += 1
	return circles
				
