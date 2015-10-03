import os
import parser as p
import sys
#tree {node : parent} (tree I)
tree , pageloadTime= p.buildTree (sys.argv[1])
# print tree
#connection ID :  parent
cTree = {}
#connectionID : list children
nodeTree = {}

def connTree (ip):
	file = 0
	fileName = 'connectionData/'
	commandTail = ' && http " -T fields -e tcp.stream  -e http.request.full_uri>'
	commandHead = 'tshark -r nytimes.pcap -Y "ip.dst == '
	for i in ip:
		com = commandHead + i + commandTail + fileName + str(file)
		line = os.popen(com , "r")
		#print line
		#print com
		f = open(fileName + str(file) , 'r')
		line = f.readline()
		lis = line.split()
		#print 'a'
		while (line != ''):
			#print 2
			if (len(lis) == 2):
				conId = int(lis[0])
				# print 'here'
				if(not(conId in cTree)):
					cTree [conId] = ip[i]
					nodeTree[conId] = []
				if(not(lis[1] in nodeTree[conId])):
					nodeTree[conId].append(lis[1])
			line = f.readline()
		f.close()
		file =file + 1

def reset():
	cTree = {}
	nodeTree={}

connTree (p.ip)
# print nodeTree
