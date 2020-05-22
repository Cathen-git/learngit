#python fasttree_wrapper.py <inDIR> <outDIR> aa

import os,sys

if len(sys.argv) != 4:
	print "python fasttree_wrapper.py inDIR outDIR DNA/aa"
	sys.exit(0)

inDIR = sys.argv[1]+"/"
outDIR = sys.argv[2]+"/"

if sys.argv[3] == "aa": alg = "-wag"
elif sys.argv[3] == "DNA": alg = "-nt -gtr" 	
else:
	print "Input data type: DNA or aa"
	sys.exit()

for alignment in os.listdir(inDIR):
	if alignment[-3:] == "fas":
		com = "FastTree "+alg+" -quiet "+inDIR+alignment
		com += " >"+outDIR+alignment+".fasttree"
		print com
		os.system(com)
