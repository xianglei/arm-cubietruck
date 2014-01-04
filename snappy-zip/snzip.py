#!/usr/bin/python

import sys,os
import snappy
from optparse import OptionParser

def Compress(Input):
	Output = Input + '.snappy'
	file_in = file(Input, "r")
	data = file_in.read()

	file_out = file(Output, "w")
	c_data = snappy.compress(data)
	file_out.write(c_data)
	file_out.close()

	file_in.close()

def Decompress(Input):
	Output = Input + '.unsnappy'
	file_in = file(Input, "r")
	c_data = file_in.read()

	file_out = file(Output, "w")
	data = snappy.decompress(c_data)
	file_out.write(data)
	file_out.close()

	file_in.close()

if __name__ == "__main__":
	usage = 'Usage: %prog -h or --help for help.'
	parser = OptionParser(usage = usage)

	parser.add_option('-c', '--compress', action='store_true', dest='action', help='[C]ompress')
	parser.add_option('-d', '--decompress', action='store_false', dest='action', help='[D]ecompress')
	options, args = parser.parse_args()
	if len(sys.argv) == 1:
		print 'Type python %s -h or --help for options help.' % sys.argv[0]
	else:
		if True == options.action:
			Compress (args[0])
		elif False == options.action:
			Decompress(args[0])
		else:
			sys.exit(0)

