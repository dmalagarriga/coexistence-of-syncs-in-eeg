#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import *
import glob
import os
from os.path import join as pjoin
import spectrum
from scipy.signal import argrelextrema
from tqdm import tqdm # this is the progress bar
#from matplotlib.backends.backend_pdf import PdfPages


def comparacio(a,b):
        
	(Sepa,numa) = a.split('_')
	(pa,exta) = numa.split('.')	

	(Sepb,numb) = b.split('_')
	(pb,extb) = numb.split('.')
	value=float(pa)-float (pb)
	return int(value/abs(value))


situation=os.getenv('situation')
subject = int(os.getenv('number'))
path = os.getenv('P_Dir')
spectra_folder=os.getenv('Task_spectra')

nTrans=0

Make_Figure = 0
Write_Output = 1

#nNodes = [43,56]
nNodes=[randint(0,64) for p in range(0,10)]
#nNodes=[1]
#p=os.getenv('p')
Raw_data = 1
Smoothed_data = 0

#Load data 
#########################################################################

if situation == 'Eyes_opened':
	File_in = genfromtxt('%s/S%03iR01_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR01_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')
if situation == 'Eyes_closed':
	File_in = genfromtxt('%s/S%03iR02_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR02_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')
if situation == 'Task_1':
	File_in = genfromtxt('%s/S%03iR03_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR03_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_2':
	File_in = genfromtxt('%s/S%03iR04_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR04_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_3':
	File_in = genfromtxt('%s/S%03iR05_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR05_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_4':
	File_in = genfromtxt('%s/S%03iR06_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR06_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_5':
	File_in = genfromtxt('%s/S%03iR07_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR07_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_6':
	File_in = genfromtxt('%s/S%03iR08_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR08_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_7':
	File_in = genfromtxt('%s/S%03iR09_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR09_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_8':
	File_in = genfromtxt('%s/S%03iR10_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR10_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_9':
	File_in = genfromtxt('%s/S%03iR11_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR11_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_10':
	File_in = genfromtxt('%s/S%03iR12_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR12_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_11':
	File_in = genfromtxt('%s/S%03iR13_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR13_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_12':
	File_in = genfromtxt('%s/S%03iR14_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR14_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')


#y0 = loadtxt(infile, skip_rows=1,unpack=True)
for i in nNodes:
	#f=y0[i][nTrans:]
	if Raw_data == 1:
		A = average(File_in[i])
	elif Smoothed_data == 1:	
		A = average(File_in_2[i])
	#M = y0[i][nTrans:] - A		
		

	
# Begin plots
##################################################################
	
	#time = loadtxt(File_in, unpack=True, usecols = [0])
	time = File_in[0]
	#(pxx,freqs)=spectrum.PSD(time[nTrans:], y0[i][nTrans:]-y0[i][nTrans:].mean(),16384)
	if Raw_data == 1:
		(pxx,freqs)=spectrum.PSD(time[nTrans:], File_in[i][nTrans:]-File_in[i][nTrans:].mean(),16384)
		#(pxx,freqs)=spectrum.PSD(time[nTrans:], File_in[i][nTrans:]-File_in[i][nTrans:].mean(),1012/2)
	elif Smoothed_data == 1:
		(pxx,freqs)=spectrum.PSD(time[nTrans:], File_in_2[i][nTrans:]-File_in_2[i][nTrans:].mean(),16384)
		#(pxx,freqs)=spectrum.PSD(time[nTrans:], File_in_2[i][nTrans:]-File_in_2[i][nTrans:].mean(),1012/2)
	
	indeces, = argrelextrema(pxx, np.greater)
	
	
	peaks = sorted(pxx[indeces])
	for j in tqdm(indeces):
		if pxx[j]==peaks[len(peaks)-1]:
			pos_2nd_max=j
	
	height_2nd_max=peaks[len(peaks)-1]
	plt.yscale('log')
	#plot(freqs, 10*log10(pxx))
	plt.plot(freqs, pxx)
	
	plt.grid('on')
	#title('P= %s' %p)
	plt.xlabel('Frequency')
	plt.ylabel('PSD (1/Hz)')
	plt.xlim([0, 100])	
	plt.ylim([.01, 10000])
	
	MAXTAB1 = list(pxx)	
	MAX1= MAXTAB1.index(max(MAXTAB1))
	#MAX2=indexmax1[0]
	xs,ys =freqs[MAX1],max(MAXTAB1)
	xa,ya =freqs[pos_2nd_max],height_2nd_max 
	ax = gca()
	#ax.annotate('(Frequency = %.3f, PSD = %.3f)' %(freqs[MAX1],max(MAXTAB1)),xy=(freqs[MAX1],max(MAXTAB1)))
	ax.annotate('%.3f Hz' %(freqs[MAX1]),xy=(freqs[MAX1],max(MAXTAB1)))
	ax.annotate('%.3f Hz' %(freqs[pos_2nd_max]),xy=(freqs[pos_2nd_max],height_2nd_max))
	plot(xs,ys,marker='o')
	plot(xa,ya,marker='o')
	'''
	plt.yscale('log')
	plot(freqs, pxx)
	#plot(freqs, 10*log10(pxx))
	grid('on')
	#title('P= %s' %p)
	xlabel('Frequency')
	ylabel('PSD (1/Hz)')
	xlim([0, 100])	
	ylim([.01, 10000])
	MAXTAB1 = list(pxx)
	MAX1= MAXTAB1.index(max(MAXTAB1))
	xs,ys =freqs[MAX1],max(MAXTAB1)
	ax = gca()
	#ax.annotate('(Frequency = %.3f, PSD = %.3f)' %(freqs[MAX1],max(MAXTAB1)),xy=(freqs[MAX1],max(MAXTAB1)))
	ax.annotate('%.3f' %(freqs[MAX1]),xy=(freqs[MAX1],max(MAXTAB1)))
	plot(xs,ys,marker='o')
	#hold()
	Maxtab,Mintab = spectrum.peakdet(pxx,50)
	print Maxtab[1][0]*0.158102766798,10*log10(Maxtab[1][1])
	#print freqs[MAX1]
	#plot(Maxtab[3][0]*0.158102766798,10*log10(Maxtab[3][1]),marker='o')
	plot(Maxtab[3][0]*0.158102766798,Maxtab[3][1],marker='o')
	ax.annotate('%.3f' %(Maxtab[3][0]*0.158102766798),xy=(Maxtab[3][0]*0.158102766798,Maxtab[3][1]))
	#ax.annotate('%.3f' %(Maxtab[3][0]*0.158102766798),xy=(Maxtab[3][0]*0.158102766798,10*log10(Maxtab[3][1])))
	'''
	
	if Make_Figure == 1:
		if Raw_data == 1:
			spectrum.savefig(pjoin(path, 'Spectrum_%i_raw.eps' % (i)))	
		elif Smoothed_data == 1:
			spectrum.savefig(pjoin(path, 'Spectrum_%i_smoothed.eps' % (i)))


	
	close()	
	
#################################################################
	
	
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	if Write_Output == 1:
		if Raw_data == 1:
			file1 = 'Spectrum_%s_raw.dat' %i
		elif Smoothed_data == 1:
			file1 = 'Spectrum_%s_smoothed.dat' %i
		path_file12 = pjoin(spectra_folder, file1)
		arx1 = open(path_file12,'w')
	
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
		print('writing to file\n:')
		for j in tqdm(range(len(freqs))):
			print(freqs[j], str(pxx[j]).strip('[]'),file=arx1)
			
		arx1.close()			 
	
close()



#Arx1.close()
	
		
