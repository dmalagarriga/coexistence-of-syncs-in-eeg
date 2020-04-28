#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import * 
from matplotlib.collections import LineCollection
import glob
import os
from os.path import join as pjoin



def comparacio(a,b):
        
	(Sepa,numa) = a.split('_')
	(pa,exta) = numa.split('.')	

	(Sepb,numb) = b.split('_')
	(pb,extb) = numb.split('.')
        value=float(pa)-float (pb)
        return int(value/abs(value))

#Kv = float(os.getenv('K_Conn'))


#Analysed_Data='Filtered data'
Analysed_Data='Filtered data'
Trans=0
path = os.getenv('P_Dir')
situation=os.getenv('situation')
subject = int(os.getenv('number'))



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
	
		data_array[i] = genfromtxt(infiles[i], unpack=True)

	
		
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
			print >> fout, i+1, j+1, Correlation[i,j], Matrix[i,j]*dt
	
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
	
	
	
	for infile in infiles:
		iterator=[]
		num_columns=64
		#Load data sets
		#t = genfromtxt(infile,delimiter=',',usecols=(0,),skip_header=1)
		for i in range(1,num_columns+1):
			iterator.append(i)

		#s = genfromtxt(infile,delimiter=',',usecols=(iterator),skip_header=1)
		s = genfromtxt(infile,unpack=True,delimiter=',',usecols=(iterator),skip_header=0)
		time =genfromtxt(infile,unpack=True,delimiter=',',usecols=0,skip_header=0)
		dt = time[1]-time[0]
		
		for k in range(len(Annotations)):
			
			Range = int ((float(Annotations[k][0])/dt)+(float(Annotations[k][1])/dt) )
			
			fout=open('%s/Correlation_%s_%s.dat' %(path,Annotations[k][0],Annotations[k][2]),'w')
		
			
	
			Matrix =zeros([len(s),len(s)])
			Correlation = zeros([len(s),len(s)])
			for i in range(len(s)):
				
				for j in range(i):
					first_index = int( float(Annotations[k][0])/dt )
					a=xcorr(s[i][first_index:Range]-s[i][first_index:Range].mean(),s[j][first_index:Range]-s[j][first_index:Range].mean(),normed=True, usevlines=False, maxlags=None, ls='-', marker='None')
					#a=xcorr(s[i][16320:],s[i][16320:],normed=True, usevlines=False, maxlags=None, ls='-', marker='None')
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
					print >> fout, i+1, j+1, Correlation[i,j], Matrix[i,j]*dt
		
	
