#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from scipy import *
from scipy.signal import hilbert
from pylab import *
from numpy import * 
import glob
import os
from os.path import join as pjoin
import cmath

################################################
# Computing the PLV value:
# - First we compute the Hilbert transform to obtain the signal in real and imaginary domains
# - Second we compute the phase as the arctan of the real and imaginary components of the Hilbert transform
# - PLV = 1/N_fast*(Sum(exp(i(phase1-phase2)))), which is the complex matrix
#
################################################

def comparacio(a,b):
        
	(Sepa,numa) = a.split('_')
	(pa,exta) = numa.split('.')	

	(Sepb,numb) = b.split('_')
	(pb,extb) = numb.split('.')
        value=float(pa)-float (pb)
        return int(value/abs(value))




Trans=0
path = os.getenv('P_Dir')
situation=os.getenv('situation')
subject = int(os.getenv('number'))


nRemove=1000 # Number of elements to remove from Hilbert Transform to avoid edge effects
#Analysed_Data='Filtered data'
Analysed_Data='Filtered data'
Smoothed = 1
Filtered_alpha = 0

if(Analysed_Data == 'Prefiltered data'):
	fout2=open('%s/PLV_sync.dat' %path,'w')
	

	infiles = sorted(glob.glob( '%s/S*.txt' %path))
	T = 23.6
	fs = 173.61
	nsamples = T * fs
	dt = 0.00576

	data_array=zeros([len(infiles),nsamples])


	PLV_matrix = zeros([len(infiles),len(infiles)])
	phase=[]
	diffase=[]
	for i in range(len(infiles)):
		data_array[i] = loadtxt(infiles[i], unpack=True)
	

	for i in range(len(infiles)):
		phase.append(unwrap(angle(hilbert(data_array[i][Trans:]-data_array[i][Trans:].mean()))))


	for k in range(len(phase)):
		for j in range(k):
			diffase.append(phase[k]-phase[j])
	
			PLV_matrix[k,j] = abs(sum(exp((phase[k]-phase[j])*1j))/len(diffase[0]))
			
	
	for i in range(len(PLV_matrix)):
		for j in range(i):
			print >> fout2,i+1,j+1,PLV_matrix[i,j]

	fout2.close()
	
elif(Analysed_Data == 'Filtered data'):
	
	if Smoothed == 1:
		if situation == 'Task_1':
			Annotations =  genfromtxt('%s/S%03iR03_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
			infiles = sorted(glob.glob( '%s/S%03iR03_data_smoothed.txt' %(path,subject)))
	
		if situation == 'Task_2':
			Annotations =  genfromtxt('%s/S%03iR04_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
			infiles = sorted(glob.glob( '%s/S%03iR04_data_smoothed.txt' %(path,subject)))
	
		if situation == 'Task_3':
			infiles = sorted(glob.glob( '%s/S%03iR05_data_smoothed.txt' %(path,subject)))
			Annotations = genfromtxt('%s/S%03iR05_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)

		if situation == 'Task_4':
			infiles = sorted(glob.glob( '%s/S%03iR06_data_smoothed.txt' %(path,subject)))
			Annotations =  genfromtxt('%s/S%03iR06_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	
		if situation == 'Task_5':
			Annotations =  genfromtxt('%s/S%03iR07_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
			infiles = sorted(glob.glob( '%s/S%03iR07_data_smoothed.txt' %(path,subject)))
	
		if situation == 'Task_6':
			Annotations =  genfromtxt('%s/S%03iR08_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
			infiles = sorted(glob.glob( '%s/S%03iR08_data_smoothed.txt' %(path,subject)))
	
		if situation == 'Task_7':
			infiles = sorted(glob.glob( '%s/S%03iR09_data_smoothed.txt' %(path,subject)))
			Annotations = genfromtxt('%s/S%03iR09_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)

		if situation == 'Task_8':
			infiles = sorted(glob.glob( '%s/S%03iR10_data_smoothed.txt' %(path,subject)))
			Annotations =  genfromtxt('%s/S%03iR10_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)


		if situation == 'Task_9':
			Annotations =  genfromtxt('%s/S%03iR11_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
			infiles = sorted(glob.glob( '%s/S%03iR11_data_smoothed.txt' %(path,subject)))
	
		if situation == 'Task_10':
			Annotations =  genfromtxt('%s/S%03iR12_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
			infiles = sorted(glob.glob( '%s/S%03iR12_data_smoothed.txt' %(path,subject)))
	
		if situation == 'Task_11':
			infiles = sorted(glob.glob( '%s/S%03iR13_data_smoothed.txt' %(path,subject)))
			Annotations = genfromtxt('%s/S%03iR13_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)

		if situation == 'Task_12':
			infiles = sorted(glob.glob( '%s/S%03iR14_data_smoothed.txt' %(path,subject)))
			Annotations =  genfromtxt('%s/S%03iR14_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	
	elif Filtered_alpha == 1:	
		if situation == 'Task_1':
			Annotations =  genfromtxt('%s/S%03iR03_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
			infiles = sorted(glob.glob( '%s/S%03iR03_data_filtered_alpha.txt' %(path,subject)))
	
		if situation == 'Task_2':
			Annotations =  genfromtxt('%s/S%03iR04_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
			infiles = sorted(glob.glob( '%s/S%03iR04_data_filtered_alpha.txt' %(path,subject)))
	
		if situation == 'Task_3':
			infiles = sorted(glob.glob( '%s/S%03iR05_data_filtered_alpha.txt' %(path,subject)))
			Annotations = genfromtxt('%s/S%03iR05_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)

		if situation == 'Task_4':
			infiles = sorted(glob.glob( '%s/S%03iR06_data_filtered_alpha.txt' %(path,subject)))
			Annotations =  genfromtxt('%s/S%03iR06_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	
		if situation == 'Task_5':
			Annotations =  genfromtxt('%s/S%03iR07_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
			infiles = sorted(glob.glob( '%s/S%03iR07_data_filtered_alpha.txt' %(path,subject)))
	
		if situation == 'Task_6':
			Annotations =  genfromtxt('%s/S%03iR08_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
			infiles = sorted(glob.glob( '%s/S%03iR08_data_filtered_alpha.txt' %(path,subject)))
	
		if situation == 'Task_7':
			infiles = sorted(glob.glob( '%s/S%03iR09_data_filtered_alpha.txt' %(path,subject)))
			Annotations = genfromtxt('%s/S%03iR09_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)

		if situation == 'Task_8':
			infiles = sorted(glob.glob( '%s/S%03iR10_data_filtered_alpha.txt' %(path,subject)))
			Annotations =  genfromtxt('%s/S%03iR10_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)

		if situation == 'Task_9':
			Annotations =  genfromtxt('%s/S%03iR11_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
			infiles = sorted(glob.glob( '%s/S%03iR11_data_filtered_alpha.txt' %(path,subject)))
	
		if situation == 'Task_10':
			Annotations =  genfromtxt('%s/S%03iR12_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
			infiles = sorted(glob.glob( '%s/S%03iR12_data_filtered_alpha.txt' %(path,subject)))
	
		if situation == 'Task_11':
			infiles = sorted(glob.glob( '%s/S%03iR13_data_filtered_alpha.txt' %(path,subject)))
			Annotations = genfromtxt('%s/S%03iR13_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)

		if situation == 'Task_12':
			infiles = sorted(glob.glob( '%s/S%03iR14_data_filtered_alpha.txt' %(path,subject)))
			Annotations =  genfromtxt('%s/S%03iR14_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
		
	num_columns=64
	for infile in infiles:
		iterator=[]
		#Load data sets
		#t = loadtxt(infile, unpack=True,usecols=(0,))
		for i in range(1,num_columns+1):
			iterator.append(i)

	s = loadtxt(infile,unpack=True,delimiter=',',usecols=(iterator),skiprows=1)
	time =genfromtxt(infile,unpack=True,delimiter=',',usecols=0,skip_header=0)
	dt = time[1]-time[0]
	for k in range(len(Annotations)):
		print k, 'out of 0',len(Annotations)
		Range = int( (float(Annotations[k][0])/dt)+(float(Annotations[k][1])/dt) ) 

		fout2=open('%s/PLV_sync_%s_%s.dat' %(path,Annotations[k][0],Annotations[k][2]),'w')
		
		first_index = int(float(Annotations[k][0])/dt)
		
	
		PLV_matrix =zeros([len(s),len(s)])
		phase=[]
		diffase=[]
		for i in range(len(s)):
			phase.append(unwrap(angle(hilbert(s[i][first_index:Range]-s[i][first_index:Range].mean()))))


		for k in range(len(phase)):
			for j in range(k):
				diffase.append(phase[k]-phase[j])
	
				PLV_matrix[k,j] = abs(sum(exp((phase[k]-phase[j])*1j))/len(diffase[0]))
			
	
		for i in range(len(PLV_matrix)):
			for j in range(i):
				print >> fout2,i+1,j+1,PLV_matrix[i,j]

		fout2.close()
			
