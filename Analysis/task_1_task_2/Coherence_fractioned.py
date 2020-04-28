#!/usr/bin/python
# -*- coding: utf-8 -*-
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
import spectrum
import matplotlib.pyplot as plt
from filtering import *

################################################
# Computing the Coherence value
################################################

def comparacio(a,b):
        
	(Sepa,numa) = a.split('_')
	(pa,exta) = numa.split('.')	
	
	(Sepb,numb) = b.split('_')
	(pb,extb) = numb.split('.')
	
	value=float(pa)-float(pb)
	return int(value/abs(value))

# Which data to analyze?
# 1- Prefiltered data
# 2- Filtered data

Analysed_Data='Prefiltered data' #Prefiltered data Filtered data



path=os.getenv('P_Dir')
situation=os.getenv('situation')
subject = int(os.getenv('number'))

nRemove=1000 # Number of elements to remove from Hilbert Transform to avoid edge effects

if(Analysed_Data == 'Prefiltered data'):

	if situation == 'Task_1':
		Annotations =  genfromtxt('%s/S%03iR03_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
		infiles = sorted(glob.glob( '%s/S%03iR03_data.txt' %(path,subject)))
	
	if situation == 'Task_2':
		Annotations =  genfromtxt('%s/S%03iR04_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
		infiles = sorted(glob.glob( '%s/S%03iR04_data.txt' %(path,subject)))
	
	if situation == 'Task_3':
		infiles = sorted(glob.glob( '%s/S%03iR05_data.txt' %(path,subject)))
		Annotations = genfromtxt('%s/S%03iR05_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)

	if situation == 'Task_4':
		infiles = sorted(glob.glob( '%s/S%03iR06_data.txt' %(path,subject)))
		Annotations =  genfromtxt('%s/S%03iR06_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
	
	if situation == 'Task_5':
		Annotations =  genfromtxt('%s/S%03iR07_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
		infiles = sorted(glob.glob( '%s/S%03iR07_data.txt' %(path,subject)))
	
	if situation == 'Task_6':
		Annotations =  genfromtxt('%s/S%03iR08_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
		infiles = sorted(glob.glob( '%s/S%03iR08_data.txt' %(path,subject)))
	
	if situation == 'Task_7':
		infiles = sorted(glob.glob( '%s/S%03iR09_data.txt' %(path,subject)))
		Annotations = genfromtxt('%s/S%03iR09_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)

	if situation == 'Task_8':
		infiles = sorted(glob.glob( '%s/S%03iR10_data.txt' %(path,subject)))
		Annotations =  genfromtxt('%s/S%03iR10_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)


	if situation == 'Task_9':
		Annotations =  genfromtxt('%s/S%03iR11_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
		infiles = sorted(glob.glob( '%s/S%03iR11_data.txt' %(path,subject)))
	
	if situation == 'Task_10':
		Annotations =  genfromtxt('%s/S%03iR12_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
		infiles = sorted(glob.glob( '%s/S%03iR12_data.txt' %(path,subject)))
	
	if situation == 'Task_11':
		infiles = sorted(glob.glob( '%s/S%03iR13_data.txt' %(path,subject)))
		Annotations = genfromtxt('%s/S%03iR13_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)

	if situation == 'Task_12':
		infiles = sorted(glob.glob( '%s/S%03iR14_data.txt' %(path,subject)))
		Annotations =  genfromtxt('%s/S%03iR14_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
	
	num_columns=64
	lowcut = 8
	highcut = 60
	fs = 400

	for infile in infiles:
		iterator=[]
		#Load data sets
		#t = loadtxt(infile, unpack=True,usecols=(0,))
		for i in range(1,num_columns+1):
			iterator.append(i)

	s = loadtxt(infile,unpack=True,delimiter=',',usecols=(iterator),skiprows=1)
	time =genfromtxt(infile,unpack=True,delimiter=',',usecols=0,skip_header=1)
	dt = time[1]-time[0]
	
	Matrix =zeros([len(s),len(s)])
	Coherence = zeros([len(s),len(s)])
	
	for k in range(len(Annotations)):
		print k,'out of ',len(Annotations)
		Range = int( (float(Annotations[k][0])/dt)+(float(Annotations[k][1])/dt) ) 
		fout=open('%s/Coherence_sync_%s_%s.dat' %(path,Annotations[k][0],Annotations[k][2]),'w')
		first_index = int(float(Annotations[k][0])/dt)
	
		for i in range(len(s)):
			
			for j in range(i):
				### Apply band-pass filter!
				y1 = butter_bandpass_filter(s[i][first_index:Range]-s[i][first_index:Range].mean(), lowcut, highcut, fs, order=6)
				y2 = butter_bandpass_filter(s[j][first_index:Range]-s[j][first_index:Range].mean(), lowcut, highcut, fs, order=6)
				
				pxy, f = spectrum.coherence(time[first_index:Range],y1,y2)
				#pxy, f = spectrum.cohere(s[i],s[j],256,1./0.0058)
				#pxy, f = spectrum.coherence(time[first_index:Range],s[i][first_index:Range]-s[i][first_index:Range].mean(),s[j][first_index:Range]-s[j][first_index:Range].mean())
				#pxy, f = spectrum.cross_spectral_density(t[Trans:],s[i][Trans:]-s[i][Trans:].mean(),s[j][Trans:]-s[j][Trans:].mean())
				#pxy, f = spectrum.normalized_cross_spectral_density(t[Trans:],s[i][Trans:]-s[i][Trans:].mean(),s[j][Trans:]-s[j][Trans:].mean())
				C = list(pxy)
			
				MAX1 = C.index(max(C))
				freqlagvalue=list(f)
				#plt.plot(freqlagvalue,C)
				#plt.ylim([0,1])
				#plt.show()
				freq = freqlagvalue[MAX1]
			
				Matrix[i,j]= freq
				Coherence[i,j]=max(C)
		
			#(pxx,freqs) = spectrum.PSD(t, s[i][Trans:]-s[i][Trans:].mean(),16384)
			#plt.plot(freqs, pxx)
			#plt.xlim([0, 40])
			#plt.show()
			#MAXTAB1 = list(pxx)	
			#MAX = MAXTAB1.index(max(MAXTAB1))
			#xs,ys = freqs[MAX],max(MAXTAB1)
			#print i,xs,ys
	
		for i in range(len(Coherence)):
			for j in range(i):
				print >> fout, i+1, j+1, Coherence[i,j], Matrix[i,j]

elif(Analysed_Data == 'Filtered data'):
	if situation == 'Task_1':
		Annotations =  genfromtxt('%s/S%03iR03_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
		infiles = sorted(glob.glob( '%s/S%03iR03_data_smoothed.txt' %(path,subject)))
	
	if situation == 'Task_2':
		Annotations =  genfromtxt('%s/S%03iR04_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
		infiles = sorted(glob.glob( '%s/S%03iR04_data_smoothed.txt' %(path,subject)))
	
	if situation == 'Task_3':
		infiles = sorted(glob.glob( '%s/S%03iR05_data_smoothed.txt' %(path,subject)))
		Annotations = genfromtxt('%s/S%03iR05_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)

	if situation == 'Task_4':
		infiles = sorted(glob.glob( '%s/S%03iR06_data_smoothed.txt' %(path,subject)))
		Annotations =  genfromtxt('%s/S%03iR06_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
	
	if situation == 'Task_5':
		Annotations =  genfromtxt('%s/S%03iR07_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
		infiles = sorted(glob.glob( '%s/S%03iR07_data_smoothed.txt' %(path,subject)))
	
	if situation == 'Task_6':
		Annotations =  genfromtxt('%s/S%03iR08_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
		infiles = sorted(glob.glob( '%s/S%03iR08_data_smoothed.txt' %(path,subject)))
	
	if situation == 'Task_7':
		infiles = sorted(glob.glob( '%s/S%03iR09_data_smoothed.txt' %(path,subject)))
		Annotations = genfromtxt('%s/S%03iR09_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)

	if situation == 'Task_8':
		infiles = sorted(glob.glob( '%s/S%03iR10_data_smoothed.txt' %(path,subject)))
		Annotations =  genfromtxt('%s/S%03iR10_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)


	if situation == 'Task_9':
		Annotations =  genfromtxt('%s/S%03iR11_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
		infiles = sorted(glob.glob( '%s/S%03iR11_data_smoothed.txt' %(path,subject)))
	
	if situation == 'Task_10':
		Annotations =  genfromtxt('%s/S%03iR12_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
		infiles = sorted(glob.glob( '%s/S%03iR12_data_smoothed.txt' %(path,subject)))
	
	if situation == 'Task_11':
		infiles = sorted(glob.glob( '%s/S%03iR13_data_smoothed.txt' %(path,subject)))
		Annotations = genfromtxt('%s/S%03iR13_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)

	if situation == 'Task_12':
		infiles = sorted(glob.glob( '%s/S%03iR14_data_smoothed.txt' %(path,subject)))
		Annotations =  genfromtxt('%s/S%03iR14_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
	
	num_columns=64
	for infile in infiles:
		iterator=[]
		#Load data sets
		#t = loadtxt(infile, unpack=True,usecols=(0,))
		for i in range(1,num_columns+1):
			iterator.append(i)

	s = loadtxt(infile,unpack=True,delimiter=',',usecols=(iterator),skiprows=1)
	time =genfromtxt(infile,unpack=True,delimiter=',',usecols=0,skip_header=1)
	dt = time[1]-time[0]
	
	Matrix =zeros([len(s),len(s)])
	Coherence = zeros([len(s),len(s)])
	
	for k in range(len(Annotations)):
		
		Range = int( (float(Annotations[k][0])/dt)+(float(Annotations[k][1])/dt) ) 
		fout=open('%s/Coherence_sync_%s_%s.dat' %(path,Annotations[k][0],Annotations[k][2]),'w')
		first_index = int(float(Annotations[k][0])/dt)
	
		for i in range(len(s)):
			
			for j in range(i):
			
				#pxy, f = spectrum.cohere(s[i],s[j],256,1./0.0058)
				pxy, f = spectrum.coherence(time[first_index:Range],s[i][first_index:Range]-s[i][first_index:Range].mean(),s[j][first_index:Range]-s[j][first_index:Range].mean())
				#pxy, f = spectrum.cross_spectral_density(t[Trans:],s[i][Trans:]-s[i][Trans:].mean(),s[j][Trans:]-s[j][Trans:].mean())
				#pxy, f = spectrum.normalized_cross_spectral_density(t[Trans:],s[i][Trans:]-s[i][Trans:].mean(),s[j][Trans:]-s[j][Trans:].mean())
				C = list(pxy)
			
				MAX1 = C.index(max(C))
				freqlagvalue=list(f)
				#plt.plot(freqlagvalue,C)
				#plt.ylim([0,1])
				#plt.show()
				freq = freqlagvalue[MAX1]
			
				Matrix[i,j]= freq
				Coherence[i,j]=max(C)
		
			#(pxx,freqs) = spectrum.PSD(t, s[i][Trans:]-s[i][Trans:].mean(),16384)
			#plt.plot(freqs, pxx)
			#plt.xlim([0, 40])
			#plt.show()
			#MAXTAB1 = list(pxx)	
			#MAX = MAXTAB1.index(max(MAXTAB1))
			#xs,ys = freqs[MAX],max(MAXTAB1)
			#print i,xs,ys
	
		for i in range(len(Coherence)):
			for j in range(i):
				print >> fout, i+1, j+1, Coherence[i,j], Matrix[i,j]	
	
