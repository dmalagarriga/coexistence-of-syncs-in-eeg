#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import *
import sys
sys.path.append("/Volumes/Backup_CRG/Dropbox_contents/CRG/Simulations/AGENT/CLOSED_LOOP/Continuous_model_from_discrete/OSN/Analysis")
use('Agg')
from filtering import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import * 
import scipy
import os
import pylab
import networkx as nx
import sys
from os.path import join as pjoin
import warnings
import collections
import itertools
import glob

situation=os.getenv('situation')
subject = int(os.getenv('number'))
path = '%s/S%03i/' %(situation,subject)

Savitzky = 1
Butterworth_alpha = 0
Butterworth_gamma = 0

if situation == 'Eyes_opened':
	File = genfromtxt('%s/S%03iR01_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR01_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR01_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR01_data_filtered_gamma.txt' %(path,subject),'w')


if situation == 'Eyes_closed':
	File = genfromtxt('%s/S%03iR02_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR02_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR02_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR02_data_filtered_gamma.txt' %(path,subject),'w')

if situation == 'Task_1':
	File = genfromtxt('%s/S%03iR03_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR03_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR03_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR03_data_filtered_gamma.txt' %(path,subject),'w')

if situation == 'Task_2':
	File = genfromtxt('%s/S%03iR04_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR04_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR04_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR04_data_filtered_gamma.txt' %(path,subject),'w')

if situation == 'Task_3':
	File = genfromtxt('%s/S%03iR05_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR05_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR05_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR05_data_filtered_gamma.txt' %(path,subject),'w')

if situation == 'Task_4':
	File = genfromtxt('%s/S%03iR06_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR06_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR06_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR06_data_filtered_gamma.txt' %(path,subject),'w')

if situation == 'Task_5':
	File = genfromtxt('%s/S%03iR07_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR07_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR07_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR07_data_filtered_gamma.txt' %(path,subject),'w')

if situation == 'Task_6':
	File = genfromtxt('%s/S%03iR08_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR08_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR08_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR08_data_filtered_gamma.txt' %(path,subject),'w')

if situation == 'Task_7':
	File = genfromtxt('%s/S%03iR09_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR09_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR09_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR09_data_filtered_gamma.txt' %(path,subject),'w')

if situation == 'Task_8':
	File = genfromtxt('%s/S%03iR10_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR10_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR10_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR10_data_filtered_gamma.txt' %(path,subject),'w')

if situation == 'Task_9':
	File = genfromtxt('%s/S%03iR11_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR11_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR11_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR11_data_filtered_gamma.txt' %(path,subject),'w')

if situation == 'Task_10':
	File = genfromtxt('%s/S%03iR12_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR12_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR12_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR12_data_filtered_gamma.txt' %(path,subject),'w')

if situation == 'Task_11':
	File = genfromtxt('%s/S%03iR13_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR13_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR13_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR13_data_filtered_gamma.txt' %(path,subject),'w')

if situation == 'Task_12':
	File = genfromtxt('%s/S%03iR14_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	if Savitzky == 1:
		File_out=open('%s/S%03iR14_data_smoothed.txt' %(path,subject),'w')
	elif Butterworth_alpha == 1:
		File_out=open('%s/S%03iR14_data_filtered_alpha.txt' %(path,subject),'w')
	elif Butterworth_gamma == 1:
		File_out=open('%s/S%03iR14_data_filtered_gamma.txt' %(path,subject),'w')

if Savitzky == 1:
	
	a,b = len(File),len(File[0])
	Signals = zeros([a,b])
	Signals[0] = File[0]
	for i in range(1,len(File)):
		Signals[i] = savitzky_golay(File[i],511,2)
	savetxt(File_out,Signals.transpose(),'%5.6f',delimiter=',')

elif Butterworth_alpha == 1:
	lowcut = 8.0
	highcut = 15.0
	fs = 500
	
	a,b = len(File),len(File[0])
	Signals = zeros([a,b])
	Signals[0] = File[0]
	for i in range(1,len(File)):
		Signals[i] = butter_bandpass_filter(File[i], lowcut, highcut, fs, order=6)
	savetxt(File_out,Signals.transpose(),'%5.6f',delimiter=',')
	
elif Butterworth_gamma == 1:

	lowcut = 8.0
	highcut = 15.0
	fs = 500
	
	a,b = len(File),len(File[0])
	Signals = zeros([a,b])
	Signals[0] = File[0]
	for i in range(1,len(File)):
		Signals[i] = butter_bandpass_filter(File[i], lowcut, highcut, fs, order=6)
	savetxt(File_out,Signals.transpose(),'%5.6f',delimiter=',')

