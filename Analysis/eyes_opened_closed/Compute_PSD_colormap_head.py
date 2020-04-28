#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import *
import glob
import os
from os.path import join as pjoin
import spectrum
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import matplotlib.mlab as ml
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
task_spectra_folder = os.getenv('Task_spectra')
nTrans=10

Frequencies = ['alpha','gamma']

nNodes=64
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
	Annotations =  np.genfromtxt('%s/S%03iR03_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	File_in = genfromtxt('%s/S%03iR03_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR03_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_2':
	Annotations =  np.genfromtxt('%s/S%03iR04_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	File_in = genfromtxt('%s/S%03iR04_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR04_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_3':
	Annotations =  np.genfromtxt('%s/S%03iR05_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	File_in = genfromtxt('%s/S%03iR05_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR05_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_4':
	Annotations =  np.genfromtxt('%s/S%03iR06_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	File_in = genfromtxt('%s/S%03iR06_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR06_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_5':
	Annotations =  np.genfromtxt('%s/S%03iR07_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	File_in = genfromtxt('%s/S%03iR07_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR07_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_6':
	Annotations =  np.genfromtxt('%s/S%03iR08_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	File_in = genfromtxt('%s/S%03iR08_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR08_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_7':
	Annotations =  np.genfromtxt('%s/S%03iR09_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	File_in = genfromtxt('%s/S%03iR09_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR09_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_8':
	Annotations =  np.genfromtxt('%s/S%03iR10_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	File_in = genfromtxt('%s/S%03iR10_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR10_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_9':
	Annotations =  np.genfromtxt('%s/S%03iR11_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	File_in = genfromtxt('%s/S%03iR11_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR11_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_10':
	Annotations =  np.genfromtxt('%s/S%03iR12_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	File_in = genfromtxt('%s/S%03iR12_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR12_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_11':
	Annotations =  np.genfromtxt('%s/S%03iR13_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	File_in = genfromtxt('%s/S%03iR13_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR13_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

if situation == 'Task_12':
	Annotations =  np.genfromtxt('%s/S%03iR14_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	File_in = genfromtxt('%s/S%03iR14_data.txt' %(path,subject),unpack=True,delimiter=',', skip_header=1)
	File_in_2 = genfromtxt('%s/S%03iR14_data_smoothed.txt' %(path,subject),unpack=True,delimiter=',')

states = ['T0','T1','T2']
position_T0 = []
position_T1 = []
position_T2 = []

if situation != 'Eyes_opened' and situation != 'Eyes_closed':
	for k in range(len(Annotations)):
		if Annotations[k][2] == 'T0':
			position_T0.append(k)
		if Annotations[k][2] == 'T1':
			position_T1.append(k)
		if Annotations[k][2] == 'T2':
			position_T2.append(k)

position = {0: array([ 180.277522,  225.45469]), 1: array([ 220.00722902,  228.171759]), 2: array([ 260.02444163,  230.0753502 ]), 3: array([ 300.03866965,  233.05350777]), 4: array([ 340.05418571,  230.06434111]), 5: array([ 380.01483072,  228.03209187]), 6: array([ 420.04004927,  225.09685106]), 
7: array([ 172.07499081,  275.08609743]), 8: array([ 215.05504516,  275.08609743]), 9: array([ 257.0581071,  275.08609743]), 10: array([ 297.05759269,  275.08609743 ]), 11: array([ 340.06120843, 275.08609743]), 12: array([ 385.06929907,  275.08609743]), 13: array([ 425.0746344 ,  275.08609743]), 
14: array([ 180.277522,  325.03091201]), 15: array([ 220.00722902,  322.03091201]), 16: array([ 260.02444163,  320.03091201]), 17: array([ 300.03866965,  318.03091201]), 18: array([340.05418571,  320.03091201]), 19: array([ 380.01483072,  322.03091201]), 20: array([ 420.04004927 ,  325.03091201]), 
21: array([ 250.00722902,  105]), 22: array([ 300.03866965, 100 ]), 23: array([ 350.05840647,  105.07716728]), 
24: array([ 200.09722856,  133.0636544 ]), 25: array([ 240.00722902,  140.02407744]), 26: array([ 300.03866965,  141.06229299]), 27: array([ 360.07697474,  140.02166359]), 28: array([ 400.00957876,  135.05148141]), 
29: array([ 160.05273126,  170.09535101]), 30: array([ 193.0564177 ,  178.06466564]), 31: array([ 233.07237285,  183.        ]), 32: array([ 263.09216978,  187.05848694]), 33: array([ 297.03866965,  188.04115495]), 34: array([ 333.08349278,  187.04933512]), 35: array([ 370.04237352,  183.04105252]), 36: array([ 410.06692057,  178.00434408]), 37: array([ 443.01567001,  170.08124302]),
38: array([ 139.09287797,  220.45469]), 39: array([ 465.04004927,  220.45469]), 
40: array([ 130.09287797,  275.08609743]), 41: array([ 470.04004927,  275.08609743]), 
42: array([ 85.03812912,  275.08609743]), 43: array([ 515.0599696 ,  275.08609743]), 
44: array([ 139.09287797,  330.03091201]), 45: array([ 465.04004927 ,  330.030912018]), 
46: array([ 160.05273126,  383.00691517]), 47: array([ 193.0564177,  377.00691517]), 48: array([ 233.07237285,  370.00691517]), 49: array([ 263.09216978,  365.00691517]), 50: array([ 300.03866965,  360.00691517 ]), 51: array([ 333.08349278 ,  365.00691517]), 52: array([ 370.04237352,  370.00691517]), 53: array([ 410.06692057,  377.00691517]), 54: array([443.01567001,  383.00691517]), 
55: array([ 200.09722856,  420.00092204]), 56: array([ 240.00722902,  407.00439586]), 57: array([ 300.03866965,  410.04843548]), 58: array([ 360.07697474,  407.05637171]), 59: array([ 400.00957876,  420.00092204]),
60: array([ 250.00722902 ,  448.07071622]), 61: array([ 300.03866965,  455.00095066]), 62: array([ 350.05840647,  448.07197886]), 
63: array([ 300.03866965,  500.08420475])}#, 64: array([ 0.06108541,  0.06567389]), 65: array([ 0.05960185,  0.0956992 ]), 66: array([ 0.03633343,  0.05853592]), 67: array([ 0.07743313,  0.04829051]), 68: array([ 0.        ,  0.05866004]), 69: array([ 0.09708561,  0.04884912]), 70: array([ 0.01750468,  0.0312812 ]), 71: array([ 0.1      ,  0.0341625]), 72: array([ 0.07889184,  0.05353793]), 73: array([ 0.05978063,  0.07012536]), 74: array([ 0.01241063,  0.03331976]), 75: array([ 0.05342753,  0.09436357]), 76: array([ 0.05876311,  0.06644972]), 77: array([ 0.02750838,  0.01507112]), 78: array([ 0.01385156,  0.06392398]), 79: array([ 0.06621961,  0.00647077]), 80: array([ 0.01287236,  0.03147086]), 81: array([ 0.02336518,  0.07948883]), 82: array([ 0.00953532,  0.03230657]), 83: array([ 0.01804648,  0.08990819]), 84: array([ 0.08058014,  0.0904769 ]), 85: array([ 0.003309  ,  0.06884944]), 86: array([ 0.00950546,  0.07820378]), 87: array([ 0.07683669,  0.00485011]), 88: array([ 0.07270306,  0.02099295]), 89: array([ 0.08184965,  0.01078525]), 90: array([ 0.0075755 ,  0.01805681]), 91: array([ 0.00072032,  0.03368326]), 92: array([ 0.02174963,  0.01079548]), 93: array([ 0.07910862,  0.02134963]), 94: array([ 0.01228009,  0.06331738]), 95: array([ 0.0746584 ,  0.02159275]), 96: array([ 0.05927043,  0.07378723]), 97: array([ 0.01025312,  0.03471603]), 98: array([ 0.0722573 ,  0.04345764]), 99: array([ 0.08054124,  0.01462422]),99: array([ 0.08054124,  0.01462422])}  


Total_positions = [position_T0, position_T1, position_T2]
Total_states = [states[0],states[1],states[2]]

for Frequency in Frequencies:
	if situation == 'Eyes_opened' or situation == 'Eyes_closed':
		pos_x = []
		pos_y = []
		power = []
		for i in tqdm(range(1,nNodes+1)):
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
				#(pxx,freqs)=spectrum.PSD(time[nTrans:], File_in[i][nTrans:]-File_in[i][nTrans:].mean(),16384)
				(pxx,freqs)=spectrum.PSD(time[nTrans:], File_in[i][nTrans:]-File_in[i][nTrans:].mean(),1012)
			elif Smoothed_data == 1:
				#(pxx,freqs)=spectrum.PSD(time[nTrans:], File_in_2[i][nTrans:]-File_in_2[i][nTrans:].mean(),16384)
				(pxx,freqs)=spectrum.PSD(time[nTrans:], File_in_2[i][nTrans:]-File_in_2[i][nTrans:].mean(),1012)
		
			
			if Frequency == 'alpha':
				for freq in freqs:
					if freq > 10.0 and freq < 10.2:
						pos_x.append(position[i-1][0])
						pos_y.append(position[i-1][1])
						power.append(10*log10(list(pxx)[list(freqs).index(freq)]))
			elif Frequency == 'gamma':
				for freq in freqs:
					if freq > 40.0 and freq < 40.2:
						pos_x.append(position[i-1][0])
						pos_y.append(position[i-1][1])
						power.append(10*log10(list(pxx)[list(freqs).index(freq)]))
			'''
			if Raw_data == 1:
				spectrum.savefig(pjoin(path, 'Spectrum_head_raw.eps' ))	
			elif Smoothed_data == 1:
				spectrum.savefig(pjoin(path, 'Spectrum_head_smoothed.eps'))
			'''
			#spectrum.savefig(pjoin(path, 'Spectrum_%s.eps' % (p)))	


		N = 1000             # number of points for interpolation
		xy_center = [pos_x[10],pos_y[10]]   # center of the plot
		radius = pos_y[63]-pos_y[10]#sqrt( (max(pos_x) - max(pos_x)/2)**2 + (max(pos_y) - max(pos_y)/2)**2 )  



		# make figure
		fig = plt.figure()

		pos_x = np.r_[pos_x,pos_x[10]-radius,pos_x[10]+radius]
		pos_x = np.r_[pos_x,pos_x[10]-radius,pos_x[10]+radius]
		pos_y = np.r_[pos_y,pos_y[10]+radius,pos_y[10]-radius]
		pos_y = np.r_[pos_y,pos_y[10]-radius,pos_y[10]+radius]
		power = np.r_[power,power[0],power[-1]]
		power = np.r_[power,power[-1],power[0]]

		# set aspect = 1 to make it a circle
		ax = fig.add_subplot(111, aspect = 1)
		xi = linspace(pos_x[10]-radius,pos_x[10]+radius,N);
		yi = linspace(pos_y[10]-radius,pos_y[10]+radius,N);
		zi = griddata((pos_x, pos_y), power, (xi[None,:], yi[:,None]), method='cubic')	
		#zi = ml.griddata(pos_x, pos_y, power, xi, yi, interp='nn')	

		# set points > radius to not-a-number. They will not be plotted.
		# the dr/2 makes the edges a bit smoother
		dr = xi[1] - xi[0]
		for i in range(N):
			for j in range(N):
				#r = sqrt((xi[i] - xy_center[0])**2 + (yi[j] - xy_center[1])**2)
				r = sqrt((xi[i] - xy_center[0])**2 + (yi[j] - xy_center[1])**2)
				if (r - dr/2) > radius:
					zi[j,i] = "nan"

		CS = plt.contourf(xi,yi,zi,15,cmap=plt.cm.jet, zorder = 1)
		ax.contour(xi, yi, zi, 15, colors = "grey", zorder = 2)
		# make a color bar
		cbar = fig.colorbar(CS, ax=ax)
		# add the data points
		# I guess there are no data points outside the head...

		ax.scatter(pos_x[:len(pos_x)-4], pos_y[:len(pos_y)-4], marker = 'o', edgecolor = "k",facecolor = 'w', s = 50, zorder = 3)
		for i in range(nNodes):
			ax.annotate(i,(pos_x[i],pos_y[i]))
		# draw a circle
		# change the linewidth to hide the 
		circle = matplotlib.patches.Circle(xy = xy_center, radius = radius, edgecolor = "k", facecolor = "none")
		ax.add_patch(circle)

		# make the axis invisible 
		for loc, spine in ax.spines.items():
			# use ax.spines.items() in Python 3
			spine.set_linewidth(0)

		# remove the ticks
		ax.set_xticks([])
		ax.set_yticks([])

		# Add some body parts. Hide unwanted parts by setting the zorder low
		# add two ears
		circle = matplotlib.patches.Ellipse(xy = [pos_x[10]+radius,pos_y[10]], width = 50.5, height = 100.0, angle = 0, edgecolor = "k", facecolor = "w", zorder = 0)
		ax.add_patch(circle)
		circle = matplotlib.patches.Ellipse(xy = [pos_x[10]-radius,pos_y[10]], width = 50.5, height = 100.0, angle = 0, edgecolor = "k", facecolor = "w", zorder = 0)
		ax.add_patch(circle)
		# add a nose
		xy = [[pos_x[10]-25,pos_y[10]-radius], [pos_x[10],pos_y[10]-radius-50],[pos_x[10]+25,pos_y[10]-radius]]
		polygon = matplotlib.patches.Polygon(xy = xy, edgecolor = "k",facecolor = "w",  zorder = 3)
		ax.add_patch(polygon) 

		# set axes limits
		ax.set_xlim(pos_x[10]-1.5*radius, pos_x[10]+1.5*radius)
		ax.set_ylim(pos_y[10]-1.5*radius, pos_y[10]+1.5*radius)
		plt.gca().invert_yaxis()
		plt.gca().invert_xaxis()
		plt.tight_layout()
		if Frequency == 'alpha':
			plt.savefig('%s/Topographic_EEG_alpha.eps' %task_spectra_folder)
		elif Frequency == 'gamma':
			plt.savefig('%s/Topographic_EEG_gamma.eps' %task_spectra_folder)
		#plt.show()	
		#################################################################
		
		
		#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

		
		#close()



		#Arx1.close()
	else:
		pos_x = []
		pos_y = []
		power_T0 = []
		power_T1 = []
		power_T2 = []
		
		for i in tqdm(range(1,nNodes+1)):
			Matrix_T0 = []
			Matrix_T1 = []
			Matrix_T2 = []
			time = File_in[0]
			dt = time[1]-time[0]
			for k in range(len(Annotations)):
				
				Range = int ((float(Annotations[k][0])/dt)+(float(Annotations[k][1])/dt) )

			
				#f=y0[i][nTrans:]
				if Raw_data == 1:
					A = average(File_in[i])
				elif Smoothed_data == 1:	
					A = average(File_in_2[i])
				#M = y0[i][nTrans:] - A		
			
				first_index = int( float(Annotations[k][0])/dt )
		
				# Begin plots
				##################################################################
		
				#time = loadtxt(File_in, unpack=True, usecols = [0])
				
				#(pxx,freqs)=spectrum.PSD(time[nTrans:], y0[i][nTrans:]-y0[i][nTrans:].mean(),16384)
				if Raw_data == 1:
					#(pxx,freqs)=spectrum.PSD(time[nTrans:], File_in[i][nTrans:]-File_in[i][nTrans:].mean(),16384)
					(pxx,freqs)=spectrum.PSD(time[first_index:Range], File_in[i][first_index:Range]-File_in[i][first_index:Range].mean(),1012)
				elif Smoothed_data == 1:
					#(pxx,freqs)=spectrum.PSD(time[nTrans:], File_in_2[i][nTrans:]-File_in_2[i][nTrans:].mean(),16384)
					(pxx,freqs)=spectrum.PSD(time[first_index:Range], File_in_2[i][first_index:Range]-File_in_2[i][first_index:Range].mean(),1012)
		
				if Annotations[k][2] == 'T0':
					Matrix_T0.append(pxx)
				elif Annotations[k][2] == 'T1':
					Matrix_T1.append(pxx)
				elif Annotations[k][2] == 'T2':
					Matrix_T2.append(pxx)
				#MAXTAB1 = list(pxx)
				#MAX1= MAXTAB1.index(max(MAXTAB1))
				#xs,ys =freqs[MAX1],max(MAXTAB1)
		
				#Maxtab,Mintab = spectrum.peakdet(pxx,50)
				#plot(Maxtab[3][0]*0.158102766798,10*log10(Maxtab[3][1]),marker='o')
				#print freqs
			Average_T0 = array(Matrix_T0).sum(axis=0)/len(Matrix_T0)
			Average_T1 = array(Matrix_T1).sum(axis=0)/len(Matrix_T1)
			Average_T2 = array(Matrix_T2).sum(axis=0)/len(Matrix_T2)
			#print len(Average_T0),len(pxx)
			
			if Frequency == 'alpha':
				for freq in freqs:
					if freq > 10.0 and freq < 10.2:
						pos_x.append(position[i-1][0])
						pos_y.append(position[i-1][1])
						power_T0.append(10*log10(list(Average_T0)[list(freqs).index(freq)]))
						power_T1.append(10*log10(list(Average_T1)[list(freqs).index(freq)]))
						power_T2.append(10*log10(list(Average_T2)[list(freqs).index(freq)]))
			elif Frequency == 'gamma':
				for freq in freqs:
					if freq > 40.0 and freq < 40.1:
						pos_x.append(position[i-1][0])
						pos_y.append(position[i-1][1])
						power_T0.append(10*log10(list(Average_T0)[list(freqs).index(freq)]))
						power_T1.append(10*log10(list(Average_T1)[list(freqs).index(freq)]))
						power_T2.append(10*log10(list(Average_T2)[list(freqs).index(freq)]))
						
		
		

		N = 500             # number of points for interpolation
		xy_center = [pos_x[10],pos_y[10]]   # center of the plot
		radius = pos_y[63]-pos_y[10]



		# make figure
		fig1 = plt.figure()
		fig2 = plt.figure()
		fig3 = plt.figure()
		
		pos_x = np.r_[pos_x,pos_x[10]-radius,pos_x[10]+radius]
		pos_x = np.r_[pos_x,pos_x[10]-radius,pos_x[10]+radius]
		pos_y = np.r_[pos_y,pos_y[10]+radius,pos_y[10]-radius]
		pos_y = np.r_[pos_y,pos_y[10]-radius,pos_y[10]+radius]
		power_T0 = np.r_[power_T0,power_T0[0],power_T0[-1]]
		power_T0 = np.r_[power_T0,power_T0[-1],power_T0[0]]

		power_T1 = np.r_[power_T1,power_T1[0],power_T1[-1]]
		power_T1 = np.r_[power_T1,power_T1[-1],power_T1[0]]
		
		power_T2 = np.r_[power_T2,power_T2[0],power_T2[-1]]
		power_T2 = np.r_[power_T2,power_T2[-1],power_T2[0]]
		# set aspect = 1 to make it a circle
		ax1 = fig1.add_subplot(111, aspect = 1)
		ax2 = fig2.add_subplot(111, aspect = 1)
		ax3 = fig3.add_subplot(111, aspect = 1)
		
		xi = linspace(pos_x[10]-radius,pos_x[10]+radius,N);
		yi = linspace(pos_y[10]-radius,pos_y[10]+radius,N);
		zi_T0 = griddata((pos_x, pos_y), power_T0, (xi[None,:], yi[:,None]), method='cubic')	
		zi_T1 = griddata((pos_x, pos_y), power_T1, (xi[None,:], yi[:,None]), method='cubic')
		zi_T2 = griddata((pos_x, pos_y), power_T2, (xi[None,:], yi[:,None]), method='cubic')
		#zi = ml.griddata(pos_x, pos_y, power, xi, yi, interp='nn')	

		# set points > radius to not-a-number. They will not be plotted.
		# the dr/2 makes the edges a bit smoother
		dr = xi[1] - xi[0]
		for i in range(N):
			for j in range(N):
				#r = sqrt((xi[i] - xy_center[0])**2 + (yi[j] - xy_center[1])**2)
				r = sqrt((xi[i] - xy_center[0])**2 + (yi[j] - xy_center[1])**2)
				if (r - dr/2) > radius:
					zi_T0[j,i] = "nan"
					zi_T1[j,i] = "nan"
					zi_T2[j,i] = "nan"

		CS_T0 = ax1.contourf(xi,yi,zi_T0,15,cmap=plt.cm.jet, zorder = 1)
		CS_T1 = ax2.contourf(xi,yi,zi_T1,15,cmap=plt.cm.jet, zorder = 1)
		CS_T2 = ax3.contourf(xi,yi,zi_T2,15,cmap=plt.cm.jet, zorder = 1)
		ax1.contour(xi, yi, zi_T0, 15, colors = "grey", zorder = 2)
		ax2.contour(xi, yi, zi_T1, 15, colors = "grey", zorder = 2)
		ax3.contour(xi, yi, zi_T2, 15, colors = "grey", zorder = 2)
		# make a color bar
		cbar_T0 = fig1.colorbar(CS_T0, ax=ax1)
		cbar_T1 = fig2.colorbar(CS_T1, ax=ax2)
		cbar_T2 = fig3.colorbar(CS_T2, ax=ax3)
		# add the data points
		# I guess there are no data points outside the head...

		ax1.scatter(pos_x[:len(pos_x)-4], pos_y[:len(pos_y)-4], marker = 'o', edgecolor = "k",facecolor = 'w', s = 50, zorder = 3)
		ax2.scatter(pos_x[:len(pos_x)-4], pos_y[:len(pos_y)-4], marker = 'o', edgecolor = "k",facecolor = 'w', s = 50, zorder = 3)
		ax3.scatter(pos_x[:len(pos_x)-4], pos_y[:len(pos_y)-4], marker = 'o', edgecolor = "k",facecolor = 'w', s = 50, zorder = 3)

		# draw a circle
		# change the linewidth to hide the 
		circle1 = matplotlib.patches.Circle(xy = xy_center, radius = radius, edgecolor = "k", facecolor = "none")
		circle2 = matplotlib.patches.Circle(xy = xy_center, radius = radius, edgecolor = "k", facecolor = "none")
		circle3 = matplotlib.patches.Circle(xy = xy_center, radius = radius, edgecolor = "k", facecolor = "none")
		ax1.add_patch(circle1)
		ax2.add_patch(circle2)
		ax3.add_patch(circle3)
		# make the axis invisible 
		for loc, spine in ax1.spines.iteritems():
			# use ax.spines.items() in Python 3
			spine.set_linewidth(0)
		for loc, spine in ax2.spines.iteritems():
			# use ax.spines.items() in Python 3
			spine.set_linewidth(0)
		for loc, spine in ax3.spines.iteritems():
			# use ax.spines.items() in Python 3
			spine.set_linewidth(0)
		# remove the ticks
		ax1.set_xticks([])
		ax1.set_yticks([])
		ax2.set_xticks([])
		ax2.set_yticks([])
		ax3.set_xticks([])
		ax3.set_yticks([])

		# Add some body parts. Hide unwanted parts by setting the zorder low
		# add two ears
		circle4 = matplotlib.patches.Ellipse(xy = [pos_x[10]+radius,pos_y[10]], width = 50.5, height = 100.0, angle = 0, edgecolor = "k", facecolor = "w", zorder = 0)
		circle5 = matplotlib.patches.Ellipse(xy = [pos_x[10]+radius,pos_y[10]], width = 50.5, height = 100.0, angle = 0, edgecolor = "k", facecolor = "w", zorder = 0)
		circle6= matplotlib.patches.Ellipse(xy = [pos_x[10]+radius,pos_y[10]], width = 50.5, height = 100.0, angle = 0, edgecolor = "k", facecolor = "w", zorder = 0)

		ax1.add_patch(circle4)
		ax2.add_patch(circle5)
		ax3.add_patch(circle6)
		
		circle7 = matplotlib.patches.Ellipse(xy = [pos_x[10]-radius,pos_y[10]], width = 50.5, height = 100.0, angle = 0, edgecolor = "k", facecolor = "w", zorder = 0)
		circle8 = matplotlib.patches.Ellipse(xy = [pos_x[10]-radius,pos_y[10]], width = 50.5, height = 100.0, angle = 0, edgecolor = "k", facecolor = "w", zorder = 0)
		circle9 = matplotlib.patches.Ellipse(xy = [pos_x[10]-radius,pos_y[10]], width = 50.5, height = 100.0, angle = 0, edgecolor = "k", facecolor = "w", zorder = 0)

		ax1.add_patch(circle7)
		ax2.add_patch(circle8)
		ax3.add_patch(circle9)
		# add a nose
		xy = [[pos_x[10]-25,pos_y[10]-radius], [pos_x[10],pos_y[10]-radius-50],[pos_x[10]+25,pos_y[10]-radius]]
		polygon1 = matplotlib.patches.Polygon(xy = xy, edgecolor = "k",facecolor = "w",  zorder = 3)
		polygon2 = matplotlib.patches.Polygon(xy = xy, edgecolor = "k",facecolor = "w",  zorder = 3)
		polygon3 = matplotlib.patches.Polygon(xy = xy, edgecolor = "k",facecolor = "w",  zorder = 3)
		ax1.add_patch(polygon1)
		ax2.add_patch(polygon2)
		ax3.add_patch(polygon3)

		# set axes limits
		ax1.set_xlim(pos_x[10]-1.5*radius, pos_x[10]+1.5*radius)
		ax1.set_ylim(pos_y[10]-1.5*radius, pos_y[10]+1.5*radius)
		
		ax2.set_xlim(pos_x[10]-1.5*radius, pos_x[10]+1.5*radius)
		ax2.set_ylim(pos_y[10]-1.5*radius, pos_y[10]+1.5*radius)
		
		ax3.set_xlim(pos_x[10]-1.5*radius, pos_x[10]+1.5*radius)
		ax3.set_ylim(pos_y[10]-1.5*radius, pos_y[10]+1.5*radius)
		
		fig1.gca().invert_yaxis()
		fig1.gca().invert_xaxis()
		fig1.tight_layout()
		
		fig2.gca().invert_yaxis()
		fig2.gca().invert_xaxis()
		fig2.tight_layout()
		
		fig3.gca().invert_yaxis()
		fig3.gca().invert_xaxis()
		fig3.tight_layout()

		print('Plotting files...\n')
		if Frequency == 'alpha':
			fig1.savefig('%s/Topographic_EEG_alpha_T0.eps' %task_spectra_folder)
			plt.close()
			fig2.savefig('%s/Topographic_EEG_alpha_T1.eps' %task_spectra_folder)
			plt.close()
			fig3.savefig('%s/Topographic_EEG_alpha_T2.eps' %task_spectra_folder)
			plt.close()
		elif Frequency == 'gamma':
			fig1.savefig('%s/Topographic_EEG_gamma_T0.eps' %task_spectra_folder)
			plt.close()
			fig2.savefig('%s/Topographic_EEG_gamma_T1.eps' %task_spectra_folder)
			plt.close()
			fig3.savefig('%s/Topographic_EEG_gamma_T2.eps' %task_spectra_folder)
			plt.close()
		#plt.show()	
		#################################################################


		#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

		
			#close()



			#Arx1.close()
	
		
