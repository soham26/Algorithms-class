"""

Algorithm for quick union:
Here, we form tree structures of connected nodes. Each node initially is its own root. As nodes are joined, their root changes to the parent root

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
	
def union(child,parent):
	rt[child]=root_node(parent)
	
#********************************************************THE END************************************************************************************
