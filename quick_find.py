# Algorithm for solving dynamic connectivity problem: Quick Find/Connected
N=input('No. of nodes')
# defining a dictionary object for indexing the nodes
ind={} 
for i in range(N):
	ind[i]=i
	# initial indexing done
#print 'The index dictionary object consisting of key-value i.e node-index pairs are\n',ind

def isconnected(p,q):
	if ind[p]==ind[q]: # checking for index matching
		return True
	else:
		return False
# function for union of two nodes, i.e connecting two nodes. Two nodes are connected if their index values are equal!
def union(p,q):
	# ind[p] and ind[q]
	# we chose a single index value to be given to both the parties. does not matter which one is chosen
	for key in ind.keys():
		if ind[key]==ind[p] or ind[key]==ind[q]:
			ind[key]=ind[p]
