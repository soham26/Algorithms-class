"""
Weighted quick union to avoid larger trees. Here, always the smaller tree is added to the larger tree, hence max distance of any node from root is less than what we find in the normal implementation of quick union.

Here we keep track of no. of objects in trees!!! Always, the tree with the smaller size gets attached to the larger tree.

Also, each time a node is being added to another tree, the whole tree is being added to the root node of tree.
"""

N=input('Enter the no. of nodes \n')
rt={} # dictionary of nodes and roots

#  A root is one which has same rt[i]==i

for i in range(N):
	rt[i]=i
	# initial indexing done

def root_node(p):
	while(rt[p]!=p):
		p=rt[p]
	return p   # returns the root of the tree
		
def isconnected(child,parent):
	#check until rt[child]==rt[parent]
	if root_node(child)==root_node(parent):
		return True
	else:
		return False

# to find size of each node tree to be added to another.
def size(p):
	p_root=root_node(p)
	sizeof_tree=0
	for i in range(N):
		if root_node(i)==p_root:
			sizeof_tree+=1
	return sizeof_tree
		
def union(child,parent):
	if size(child)<size(parent):
		rt[root_node(child)]=root_node(parent)
	else:
		rt[root_node(parent)]=root_node(child)
