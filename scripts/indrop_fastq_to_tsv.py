#!/usr/bin/python 
import sys, os 
from itertools import islice

fastqhandle = sys.argv[1]

if fastqhandle == "-": 
	sys.stderr.write('parsing fastq from stdin\n') 
	infile = sys.stdin 
else: 
	sys.stderr.write('parsing fastq from file: {}\n'.format(fastqhandle))
	infile = open(fastqhandle, 'r')


minimum_lineage_barcode_length=10

def process_record(record): 
	# sys.stderr.write('working on record: \n')
	# sys.stderr.write(str(record))
	# sys.stderr.write('\n')
	# print record
	# read_name, umi, cell_barcode = record[0].rstrip('\n').split('_')
	cell_barcode, umi, read_name = record[0].strip('@').rstrip('\n').split(':')
	lineage_barcode = record[1].rstrip('\n')

	cell_barcode = cell_barcode[-17:]
	if len(lineage_barcode) >= minimum_lineage_barcode_length:
		print "{}\t{}\t{}\t{}".format(read_name, umi, cell_barcode, lineage_barcode)


lines = []
for line in infile:
    lines.append(line)
    if len(lines) == 4:
        # print 'working on ' + str(lines)
        process_record(lines)
        lines = []
