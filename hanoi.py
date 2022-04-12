import argparse
from copy import deepcopy
import time

class Node:
	    def __init__(self,state,parent,g):
	        self.state = state
	        self.parent = parent
	        self.g = g

class Node_a:
	def __init__(self,state,parent,g,h):
		self.state = state
		self.parent = parent
		self.g = g
		self.h = h

	def setH(self,goal):
		h = 0
		for r in range(len(self.state)):
			for c in range(len(self.state[r])):
				if(self.state[r][c]!=goal[r][c]):
					h+=1
		self.h = h

def printState(current):
    print(current.state)
    print("\ng: ",current.g)
    print("------")

def printState_a(current):
    print(current.state)
    print("\ng: ",current.g)
    print("\nh: ",current.h)
    print("------")

def visited(path, current):
    visited = False
    for n in path:
        if(n.state==current.state):
            visited = True
    return visited

def findElementToMove(current, r):
	for i in range(len(current.state[r])):
		if(current.state[r][i] != 0):
			return i
	return -1

def move(current,i,j):
	child = deepcopy(current.state)
	child[j[0]][j[1]] = child[i[0]][i[1]]
	child[i[0]][i[1]] = 0
	return child

def findChilds(frontier,current,g):

	for i in range(len(current.state)):
		n = findElementToMove(current,i)
		if(n!=-1):
			for j in range(len(current.state)):
				if(i!=j):
					if(0 in current.state[j]):
						pos = -(current.state[j][::-1].index(0)-(len(current.state[j])-1))
						if(pos != (len(current.state[j])-1)):
							if(current.state[i][n] < current.state[j][pos+1]):
								frontier.append(Node(move(current,[i,n],[j,pos]),current,g))
						else:
							frontier.append(Node(move(current,[i,n],[j,pos]),current,g))

def sortChilds(childs):
    for i in range(len(childs)-1):
        for j in range(0, len(childs)-i-1):
            if((childs[j].g + childs[j].h) < (childs[j+1].g + childs[j+1].h)):
                aux = childs[j+1]
                childs[j+1] = childs[j]
                childs[j] = aux

def findChilds_a(frontier,current,g,goal):

	childs = []
	for i in range(len(current.state)):
		n = findElementToMove(current,i)
		if(n!=-1):
			for j in range(len(current.state)):
				if(i!=j):
					if(0 in current.state[j]):
						pos = -(current.state[j][::-1].index(0)-(len(current.state[j])-1))
						if(pos != (len(current.state[j])-1)):
							if(current.state[i][n] < current.state[j][pos+1]):
								child = Node_a(move(current,[i,n],[j,pos]),current,g,None)
								child.setH(goal)
								childs.append(child)

						else:
							child = Node_a(move(current,[i,n],[j,pos]),current,g,None)
							child.setH(goal)
							childs.append(child)

	sortChilds(childs)
	for a in childs:
		frontier.append(a)

def bfs(r,d):

	root = []
	goal = []

	for i in range(r):
		root.append([])
		goal.append([])
		for n in range(d):
			if(i==0):
				root[i].append(n+1)
				goal[i].append(0)
			elif(i == r-1):
				root[i].append(0)
				goal[i].append(n+1)
			else:
				root[i].append(0)
				goal[i].append(0)
	g=0
	found = False
	frontier = []
	path = []
	current = None
	i=0

	root_node= Node(root,None,0)
	print("\nThis is the initial state:")
	print(root_node.state)
	print("\nThis is the goal state:")
	print(goal)
	frontier.append(root_node)

	while not found and frontier:
		current = frontier.pop(0)
		printState(current)
		path.append(current)
		g = current.g
		if(current.state == goal):
			found = True
			break
		findChilds(frontier,current,g+1)

def bfs_g(r,d):

	root = []
	goal = []

	for i in range(r):
		root.append([])
		goal.append([])
		for n in range(d):
			if(i==0):
				root[i].append(n+1)
				goal[i].append(0)
			elif(i == r-1):
				root[i].append(0)
				goal[i].append(n+1)
			else:
				root[i].append(0)
				goal[i].append(0)
	g=0
	found = False
	frontier = []
	path = []
	current = None
	i=0

	root_node= Node(root,None,0)
	print("\nThis is the initial state:")
	print(root_node.state)
	print("\nThis is the goal state:")
	print(goal)
	frontier.append(root_node)

	while not found and frontier:
		current = frontier.pop(0)
		if(not visited(path,current)):
			printState(current)
			path.append(current)
			g = current.g
			if(current.state == goal):
				found = True
				break
			findChilds(frontier,current,g+1)

def dfs(r,d):

	root = []
	goal = []

	for i in range(r):
		root.append([])
		goal.append([])
		for n in range(d):
			if(i==0):
				root[i].append(n+1)
				goal[i].append(0)
			elif(i == r-1):
				root[i].append(0)
				goal[i].append(n+1)
			else:
				root[i].append(0)
				goal[i].append(0)
	g=0
	found = False
	frontier = []
	path = []
	current = None
	i=0

	root_node= Node(root,None,0)
	print("\nThis is the initial state:")
	print(root_node.state)
	print("\nThis is the goal state:")
	print(goal)
	frontier.append(root_node)

	while not found and frontier:
		current = frontier.pop()
		printState(current)
		path.append(current)
		g = current.g
		if(current.state == goal):
			found = True
			break
		findChilds(frontier,current,g+1)

def dfs_g(r,d):

	root = []
	goal = []

	for i in range(r):
		root.append([])
		goal.append([])
		for n in range(d):
			if(i==0):
				root[i].append(n+1)
				goal[i].append(0)
			elif(i == r-1):
				root[i].append(0)
				goal[i].append(n+1)
			else:
				root[i].append(0)
				goal[i].append(0)
	g=0
	found = False
	frontier = []
	path = []
	current = None
	i=0

	root_node= Node(root,None,0)
	print("\nThis is the initial state:")
	print(root_node.state)
	print("\nThis is the goal state:")
	print(goal)
	frontier.append(root_node)

	while not found and frontier:
		current = frontier.pop()
		if(not visited(path,current)):
			printState(current)
			path.append(current)
			g = current.g
			if(current.state == goal):
				found = True
				break
			findChilds(frontier,current,g+1)

def a_search(r,d):

	root = []
	goal = []

	for i in range(r):
		root.append([])
		goal.append([])
		for n in range(d):
			if(i==0):
				root[i].append(n+1)
				goal[i].append(0)
			elif(i == r-1):
				root[i].append(0)
				goal[i].append(n+1)
			else:
				root[i].append(0)
				goal[i].append(0)
	g=0
	found = False
	frontier = []
	path = []
	current = None
	i=0

	root_node= Node_a(root,None,0,None)
	root_node.setH(goal)
	print("\nThis is the initial state:")
	print(root_node.state)
	print("\nThis is the goal state:")
	print(goal)
	frontier.append(root_node)

	while not found and frontier:
		current = frontier.pop(0)
		if(not visited(path,current)):
			printState_a(current)
			path.append(current)
			g = current.g
			if(current.h == 0):
				found = True
				break
			findChilds_a(frontier,current,g+1,goal)

#----- Main program -----------

parser = argparse.ArgumentParser()
parser.add_argument('-r', help='Number of rods', required=True)
parser.add_argument('-d', help='Number of disks', required=True)
parser.add_argument('-s', help='Search method: bfs, bfs_g,dfs,dfs_g,a_search', required=True)
args = vars(parser.parse_args())
r = int(args['r'])
d = int(args['d'])
method = args['s']

if(r < 3):
	print("invalid r argument: r must be at least 3")
else:
	match(method):
		case 'bfs':
			media=0
			for i in range(10):
				time1 = time.time()
				bfs(r,d)
				time2 = time.time()
				media = media + (time2-time1)
				print("cost: ",time2-time1)
			print("media: ",media/10)
		case 'bfs_g':
			media = 0
			for i in range(10):
				time1 = time.time()
				bfs_g(r,d)
				time2 = time.time()
				media = media + (time2-time1)
				print("cost: ",time2-time1)
			print("media: ",media/10)
		case 'dfs':
			media = 0
			for i in range(10):
				time1 = time.time()
				dfs(r,d)
				time2 = time.time()
				media = media + (time2-time1)
				print("cost: ",time2-time1)
			print("media: ",media/10)
		case 'dfs_g':
			media = 0
			for i in range(10):
				time1 = time.time()
				dfs_g(r,d)
				time2 = time.time()
				media = media + (time2-time1)
				print("cost: ",time2-time1)
			print("media: ",media/10)
		case 'a_search':
			media = 0
			for i in range(10):
				time1 = time.time()
				a_search(r,d)
				time2 = time.time()
				media = media + (time2-time1)
				print("cost: ",time2-time1)
			print("media: ",media/10)
		case _:
			print("invalid s argument: s must be bfs, bfs_g,dfs,dfs_g")
