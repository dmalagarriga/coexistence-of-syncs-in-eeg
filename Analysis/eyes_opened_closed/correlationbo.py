#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import * 
from matplotlib.collections import LineCollection
import glob
import os
from os.path import join as pjoin
from tqdm import tqdm



def comparacio(a,b):
        
	(Sepa,numa) = a.split('_')
	(pa,exta) = numa.split('.')	

	(Sepb,numb) = b.split('_')
	(pb,extb) = numb.split('.')
	value=float(pa)-float(pb)
	return int(value/abs(value))


Analysed_Data='Filtered data' # 'Prefiltered data'
Trans=10
path = os.getenv('P_Dir')
situation=os.getenv('situation')
subject = int(os.getenv('number'))

dt = 0.00625

if(Analysed_Data == 'Prefiltered data'):
	infiles = sorted(glob.glob( '%s/F*.txt' %path))
	
	fout=open('%s/Correlation_Sorted_By_Pairs_Not_filtered.dat' %path,'w')

	T = 23.6
	fs = 173.61
	nsamples = T * fs
	dt = 0.00576

	data_array=zeros([len(infiles),nsamples])

	#for infile in infiles:
	for i in range(len(infiles)):
	
		T = 23.6
		fs = 173.61
		nsamples = T * fs
		t = np.linspace(0, T, nsamples, endpoint=False)
	
		data_array[i] = loadtxt(infiles[i], unpack=True)

	
		
	Matrix =zeros([len(infiles),len(infiles)])
	Correlation = zeros([len(infiles),len(infiles)])
	#Compute the cross correlation and plot it.
	for i in range(len(infiles)):
			
		for j in range(i):

			a=xcorr(data_array[i][Trans:]-data_array[i][Trans:].mean(),data_array[j][Trans:]-data_array[j][Trans:].mean(),normed=True, usevlines=False, maxlags=None, ls='-', marker='None')
			
		
				
			##############################
			# Compute the maximum of     #
			# the delay and its position #
			#############################
				
	
			C = list(a[1])
			MAX1 = C.index(max(C))
			lagvalue=list(a[0])
				
			lagg = lagvalue[MAX1]
			
			
			############################
			# Filling the delay matrix #
			############################
			
			Matrix[i,j]= lagg
			Correlation[i,j]=max(C)
			
			
	for i in range(len(Correlation)):
		for j in range(i):
			print(i+1, j+1, Correlation[i,j], Matrix[i,j]*dt,file=fout)
	
elif(Analysed_Data == 'Filtered data'):
	if situation == 'Eyes_opened':
		infiles = sorted(glob.glob( '%s/S%03iR01_data.txt' %(path,subject)))
	if situation == 'Eyes_closed':
		infiles = sorted(glob.glob( '%s/S%03iR02_data.txt' %(path,subject)))
	if situation == 'Task_1':
		infiles = sorted(glob.glob( '%s/S%03iR03_data.txt' %(path,subject)))
	if situation == 'Task_2':
		infiles = sorted(glob.glob( '%s/S%03iR04_data.txt' %(path,subject)))
	if situation == 'Task_3':
		infiles = sorted(glob.glob( '%s/S%03iR05_data.txt' %(path,subject)))
	if situation == 'Task_4':
		infiles = sorted(glob.glob( '%s/S%03iR06_data.txt' %(path,subject)))
	fout=open('%s/Correlation_Sorted_By_Pairs_Filtered.dat' %path,'w')
	num_columns=63
	for infile in infiles:
		iterator=[]
		#Load data sets
		#t = genfromtxt(infile,delimiter=',',usecols=(0,),skiprows=1)
		for i in range(1,num_columns+1):
			iterator.append(i)
	
		#s = genfromtxt(infile,delimiter=',',usecols=(iterator),skiprows=1)
		s = loadtxt(infile,unpack=True,delimiter=',',usecols=(iterator),skiprows=1)
	
	Matrix =zeros([len(s),len(s)])
	Correlation = zeros([len(s),len(s)])

	for i in tqdm(range(len(s))):
			
		for j in range(i):
			a=xcorr(s[i][Trans:]-s[i][Trans:].mean(),s[j][Trans:]-s[j][Trans:].mean(),normed=True, usevlines=False, maxlags=None, ls='-', marker='None')
			##############################
			# Compute the maximum of     #
			# the delay and its position #
			#############################
				
	
			C = list(a[1])
			MAX1 = C.index(max(C))
			lagvalue=list(a[0])
				
			lagg = lagvalue[MAX1]
			
			
			############################
			# Filling the delay matrix #
			############################
			
			Matrix[i,j]= lagg
			Correlation[i,j]=max(C)
	print('done!\n')

	print('Writing to file...\n')
	for i in tqdm(range(len(Correlation))):
		for j in range(i):
			#print >> fout, i+1, j+1, Correlation[i,j], Matrix[i,j]*dt
			print(i+1, j+1, Correlation[i,j], Matrix[i,j]*dt,file=fout)
	print('done!\n')
