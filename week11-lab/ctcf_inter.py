#!/usr/bin/env python

"""
Usage: ./ctcf_inter.py peaks.txt
This code looks for HiC bins that contain at least one CTCF peak.
"""

import sys
import numpy
import hifive

bin_peaks = []
bin_list = list(range(15000000, 17500000, 10000))

for line in open(sys.argv[1]):
    fields = line.rstrip('\r\n').split('\t')
    if fields[0] == 'chr17':
        start = int(fields[1])
        end = int(fields[2])
        mid_len = int((end-start)/2)
        peak = start + mid_len
        i = 0
        for num in bin_list:
            if peak in range(num, num+10000):
                if i not in bin_peaks:
                    bin_peaks.append(i)
                    
            i += 1
            
# (c-start)/binsize = i (i is the bin number)

hic = hifive.HiC('hic.hcp')
data = hic.cis_heatmap(chrom='chr17', start=15000000, stop=17500000, binsize=10000, datatype='fend', arraytype='full')

data[:, :, 1] *= numpy.sum(data[:, :, 0]) / numpy.sum(data[:, :, 1])
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = data[:, :, 0]

for num in bin_peaks:
    for var in bin_peaks:
        if data[num, var] > 1:
            print num, var, data[num, var]