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
from tqdm import tqdm # this is the progress bar

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




Trans=1000
path = os.getenv('P_Dir')
situation=os.getenv('situation')
subject = int(os.getenv('number'))


nRemove=1000 # Number of elements to remove from Hilbert Transform to avoid edge effects
#Analysed_Data='Filtered data'
Analysed_Data='Filtered data'
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
			
	print('Writing to file: \n' )
	for i in tqdm(range(len(PLV_matrix))):
		for j in range(i):
			print(i+1,j+1,PLV_matrix[i,j],file=fout2)
			

	fout2.close()
	
elif(Analysed_Data == 'Filtered data'):
	fout2=open('%s/PLV_sync.dat' %path,'w')
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
	num_columns=63
	
	for infile in infiles:
		iterator=[]
		#Load data sets
		#t = loadtxt(infile, unpack=True,usecols=(0,))
		for i in range(1,num_columns+1):
			iterator.append(i)
	
		s = loadtxt(infile,unpack=True,delimiter=',',usecols=(iterator),skiprows=1)
	
	PLV_matrix =zeros([len(s),len(s)])
	phase=[]
	diffase=[]
	for i in range(len(s)):
		phase.append(unwrap(angle(hilbert(s[i][Trans:]-s[i][Trans:].mean()))))


	for k in range(len(phase)):
		for j in range(k):
			diffase.append(phase[k]-phase[j])
	
			PLV_matrix[k,j] = abs(sum(exp((phase[k]-phase[j])*1j))/len(diffase[0]))
			
	
	print('Writing to file: \n' )
	for i in tqdm(range(len(PLV_matrix))):
		for j in range(i):
			print(i+1,j+1,PLV_matrix[i,j],file=fout2)
			

	fout2.close()
			
