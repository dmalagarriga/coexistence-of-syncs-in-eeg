#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import *
import sys
sys.path.append("/home/dmalagarriga/Dropbox (CRG)/CRG/Simulations/AGENT/CLOSED_LOOP/Continuous_model_from_discrete/OSN/Analysis")
use('Agg')
from scipy import *
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import math
import matplotlib.animation as manimation
from matplotlib.patches import Arc
from numpy import random
from random import uniform
import matplotlib.cm as cm
import time
from filtering import *
from peak_detection import *
from scipy.interpolate import griddata
import subprocess
import os
import glob
import warnings
import collections
import itertools
import matplotlib.image as mpimg
import commands
import networkx as nx
plt.rcParams['animation.ffmpeg_path'] = '/usr/bin/ffmpeg'

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=5, codec = "libx264",bitrate=-1,extra_args=['-pix_fmt', 'yuv420p'],metadata=metadata)

#OPTIONS



compute_matrices=1
nNodes=64
thresh=int(os.getenv('Threshold'))
situation=os.getenv('situation')
Coexistence=os.getenv('Coexistence')
subject = int(os.getenv('number'))
path_input = '%s/S%03i/Coexistence_pairs/Thresh_%s' %(situation,subject,thresh)
path = '%s/S%03i/' %(situation,subject)
Net_labels =  numpy.loadtxt('Task_1/S001/S001R03_signals.txt',unpack=True,delimiter=',', usecols = (0,1),dtype=('|S4','|S4'), skiprows=1)
path_network='Tasks_consistence/%s/S%03i/%s/Thresh_%s/Sync_patterns' %(situation,subject,Coexistence,thresh)
if situation == 'Task_1':
	Annotations =  numpy.genfromtxt('%s/S%03iR03_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	infiles = sorted(glob.glob( '%s/S%03iR03_data_smoothed.txt' %(path,subject)))

if situation == 'Task_2':
	Annotations =  numpy.genfromtxt('%s/S%03iR04_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
	infiles = sorted(glob.glob( '%s/S%03iR04_data_smoothed.txt' %(path,subject)))

if situation == 'Task_3':
	infiles = sorted(glob.glob( '%s/S%03iR05_data_smoothed.txt' %(path,subject)))
	Annotations = numpy.genfromtxt('%s/S%03iR05_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)

if situation == 'Task_4':
	infiles = sorted(glob.glob( '%s/S%03iR06_data_smoothed.txt' %(path,subject)))
	Annotations =  numpy.genfromtxt('%s/S%03iR06_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)

if situation == 'Task_5':
	Annotations =  numpy.genfromtxt('%s/S%03iR07_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	infiles = sorted(glob.glob( '%s/S%03iR07_data_smoothed.txt' %(path,subject)))

if situation == 'Task_6':
	Annotations =  numpy.genfromtxt('%s/S%03iR08_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
	infiles = sorted(glob.glob( '%s/S%03iR08_data_smoothed.txt' %(path,subject)))

if situation == 'Task_7':
	infiles = sorted(glob.glob( '%s/S%03iR09_data_smoothed.txt' %(path,subject)))
	Annotations = numpy.genfromtxt('%s/S%03iR09_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)

if situation == 'Task_8':
	infiles = sorted(glob.glob( '%s/S%03iR10_data_smoothed.txt' %(path,subject)))
	Annotations =  numpy.genfromtxt('%s/S%03iR10_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)


if situation == 'Task_9':
	Annotations =  numpy.genfromtxt('%s/S%03iR11_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('|S4','<f8','|S4'), skip_header=1)
	infiles = sorted(glob.glob( '%s/S%03iR11_data_smoothed.txt' %(path,subject)))

if situation == 'Task_10':
	Annotations =  numpy.genfromtxt('%s/S%03iR12_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
	infiles = sorted(glob.glob( '%s/S%03iR12_data_smoothed.txt' %(path,subject)))

if situation == 'Task_11':
	infiles = sorted(glob.glob( '%s/S%03iR13_data_smoothed.txt' %(path,subject)))
	Annotations = numpy.genfromtxt('%s/S%03iR13_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)

if situation == 'Task_12':
	infiles = sorted(glob.glob( '%s/S%03iR14_data_smoothed.txt' %(path,subject)))
	Annotations =  numpy.genfromtxt('%s/S%03iR14_annotations.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1,2),dtype=('<f8','<f8','|S4'), skip_header=1)
fig=plt.figure(num=None,figsize=(10,10))
img = mpimg.imread('64_channel_sharbrough.png')
implot = plt.imshow(img)
ax_1 = fig.add_subplot(111)
with writer.saving(fig, "prova.mpg" , 150):	
	for k in range(len(Annotations)):
		state = '%s_%s' %(Annotations[k][0],Annotations[k][2])
		if compute_matrices==1:
			Comp_Sync_List=[]
			Lag_Sync_List=[]
			Phase_Sync_List=[]
	
			#for subject in numpy.arange(1,110): 
			#for situation in ['Task_1', 'Task_5', 'Task_11']:
	


			# Phase and correlation of every node
			#Xcorr = numpy.genfromtxt('%s/Correlation_Sorted_By_Pairs_Filtered.dat' %(path),dtype=(int,int,float,float))
			#Phase = numpy.genfromtxt('%s/PLV_sync.dat' %(path),dtype=(int,int,float))

			# Classified pairs
			with warnings.catch_warnings():
				warnings.simplefilter("ignore")
				#Not_Sync = numpy.genfromtxt('%s/Only_Not_sync_pairs_XCORR_PHASE_LAG_Thresh_%s_%s.dat' %(path,thresh,state),dtype=(int,int))
				Complete_Sync = numpy.genfromtxt('%s/Only_Complete_sync_pairs_XCORR_PHASE_LAG_Thresh_%s_%s.dat' %(path_input,thresh,state),dtype=(int,int))
				Lag_Sync = numpy.genfromtxt('%s/Only_Lag_sync_pairs_XCORR_PHASE_LAG_Thresh_%s_%s.dat' %(path_input,thresh,state),dtype=(int,int))
				Phase_Sync = numpy.genfromtxt('%s/Only_Phase_sync_pairs_XCORR_PHASE_LAG_Thresh_%s_%s.dat' %(path_input,thresh,state),dtype=(int,int))
				#Gen_Syn = numpy.genfromtxt('%s/Only_Generalized_sync_pairs_XCORR_PHASE_LAG_Thresh_%s_%s.dat' %(path,thresh,state),dtype=(int,int))
	
		
			if Complete_Sync != [] or Lag_Sync != [] or Phase_Sync != []:
		
				if not Complete_Sync.any():
					Comp_Sync_List=Comp_Sync_List
				elif numpy.array(Complete_Sync).shape == (2,):
					Comp_Sync_List.append(numpy.array(Complete_Sync))
				elif numpy.array(Complete_Sync).shape == (2,2):
					Comp_Sync_List.extend(Complete_Sync)
				else:
					Comp_Sync_List.extend(Complete_Sync)
	
				if not Lag_Sync.any():	
					Lag_Sync_List=Lag_Sync_List
				elif numpy.array(Lag_Sync).shape == (2,):
		
					Lag_Sync_List.append(numpy.array(Lag_Sync))
				elif numpy.array(Lag_Sync).shape == (2,):
		
					Lag_Sync_List.extend(Lag_Sync)
				else:
					Lag_Sync_List.extend(Lag_Sync)
		
	
				if not Phase_Sync.any():
					Phase_Sync_List=Phase_Sync_List
				elif numpy.array(Phase_Sync).shape == (2,):
					Phase_Sync_List.append(Phase_Sync)
				elif numpy.array(Phase_Sync).shape == (2,2):
					Phase_Sync_List.extend(Phase_Sync)
				else:	
					Phase_Sync_List.extend(Phase_Sync)
	
	
			Pairs_and_Count_Phase = [(a,b,v) for (a,b),v in collections.Counter(map(tuple,Phase_Sync_List)).iteritems()]
			#print sorted(Pairs_and_Count_Phase,key=lambda x: x[2],reverse=True)
			Pairs_and_Count_Lag = [(a,b,v) for (a,b),v in collections.Counter(map(tuple,Lag_Sync_List)).iteritems()]
			#print sorted(Pairs_and_Count_Lag,key=lambda x: x[2],reverse=True)
			Pairs_and_Count_Comp = [(a,b,v) for (a,b),v in collections.Counter(map(tuple,Comp_Sync_List)).iteritems()]
			#print len(sorted(Pairs_and_Count_Comp,key=lambda x: x[2],reverse=True))
		
	
			Average_Count_Comp=[]
			Average_Count_Lag=[]
			Average_Count_Phase=[]
			for i,j,k in Pairs_and_Count_Comp:
		
				Average_Count_Comp.append(k)
			for i,j,k in Pairs_and_Count_Lag:
		
				Average_Count_Lag.append(k)
			for i,j,k in Pairs_and_Count_Phase:
				Average_Count_Phase.append(k)
	
			List_edges_Comp=[]
			List_edges_Lag=[]
			List_edges_Phase=[]
	
			
			#for i,j in List_edges_Comp:
			#	if (i,j) in List_edges_Lag:
			#		print 'hola'
			#print numpy.average(Average_Count_Comp),numpy.average(Average_Count_Lag),numpy.average(Average_Count_Phase)
			#print numpy.std(Average_Count_Comp),numpy.std(Average_Count_Lag),numpy.std(Average_Count_Phase)
			for i,j,k in Pairs_and_Count_Comp:
				#if k>numpy.std(Average_Count_Comp):
				List_edges_Comp.append((i-1,j-1))
			for i,j,k in Pairs_and_Count_Lag:
				#if k>2*numpy.std(Average_Count_Lag):
				List_edges_Lag.append((i-1,j-1))
			for i,j,k in Pairs_and_Count_Phase:
				#if k>2*numpy.std(Average_Count_Phase):
				List_edges_Phase.append((i-1,j-1))
			Adj_Complete_Sync=numpy.zeros([nNodes,nNodes])
			Adj_Lag_Sync=numpy.zeros([nNodes,nNodes])
			Adj_Phase_Sync=numpy.zeros([nNodes,nNodes])
			Adj_Matrix = numpy.zeros([nNodes,nNodes])
		
			for i,j,k in Pairs_and_Count_Comp:
				Adj_Complete_Sync[i-1,j-1] = float(k) # 3 are the number of coexistence elements
				Adj_Complete_Sync[j-1,i-1] = float(k)
				Adj_Matrix[i-1,j-1] = 1
				Adj_Matrix[j-1,i-1] = 1
			for i,j,k in Pairs_and_Count_Lag:
				Adj_Lag_Sync[i-1,j-1] = float(k)
				Adj_Lag_Sync[j-1,i-1] = float(k)
				Adj_Matrix[i-1,j-1] = 1
				Adj_Matrix[j-1,i-1] = 1
			for i,j,k in Pairs_and_Count_Phase:
				Adj_Phase_Sync[i-1,j-1] = float(k)
				Adj_Phase_Sync[j-1,i-1] = float(k)
				Adj_Matrix[i-1,j-1] = 1
				Adj_Matrix[j-1,i-1] = 1
	
		
			position = {0: numpy.array([ 180.277522,  225.45469]), 1: numpy.array([ 220.00722902,  228.171759]), 2: numpy.array([ 260.02444163,  230.0753502 ]), 3: numpy.array([ 300.03866965,  233.05350777]), 4: numpy.array([ 340.05418571,  230.06434111]), 5: numpy.array([ 380.01483072,  228.03209187]), 6: numpy.array([ 420.04004927,  225.09685106]), 
				7: numpy.array([ 172.07499081,  275.08609743]), 8: numpy.array([ 215.05504516,  275.08609743]), 9: numpy.array([ 257.0581071,  275.08609743]), 10: numpy.array([ 297.05759269,  275.08609743 ]), 11: numpy.array([ 340.06120843, 275.08609743]), 12: numpy.array([ 385.06929907,  275.08609743]), 13: numpy.array([ 425.0746344 ,  275.08609743]), 
				14: numpy.array([ 180.277522,  325.03091201]), 15: numpy.array([ 220.00722902,  322.03091201]), 16: numpy.array([ 260.02444163,  320.03091201]), 17: numpy.array([ 300.03866965,  318.03091201]), 18: numpy.array([340.05418571,  320.03091201]), 19: numpy.array([ 380.01483072,  322.03091201]), 20: numpy.array([ 420.04004927 ,  325.03091201]), 
				21: numpy.array([ 250.00722902,  105]), 22: numpy.array([ 300.03866965, 100 ]), 23: numpy.array([ 350.05840647,  105.07716728]), 
				24: numpy.array([ 200.09722856,  133.0636544 ]), 25: numpy.array([ 240.00722902,  140.02407744]), 26: numpy.array([ 300.03866965,  141.06229299]), 27: numpy.array([ 360.07697474,  140.02166359]), 28: numpy.array([ 400.00957876,  135.05148141]), 
				29: numpy.array([ 160.05273126,  170.09535101]), 30: numpy.array([ 193.0564177 ,  178.06466564]), 31: numpy.array([ 233.07237285,  183.        ]), 32: numpy.array([ 263.09216978,  187.05848694]), 33: numpy.array([ 297.03866965,  188.04115495]), 34: numpy.array([ 333.08349278,  187.04933512]), 35: numpy.array([ 370.04237352,  183.04105252]), 36: numpy.array([ 410.06692057,  178.00434408]), 37: numpy.array([ 443.01567001,  170.08124302]),
				38: numpy.array([ 139.09287797,  220.45469]), 39: numpy.array([ 465.04004927,  220.45469]), 
				40: numpy.array([ 130.09287797,  275.08609743]), 41: numpy.array([ 470.04004927,  275.08609743]), 
				42: numpy.array([ 85.03812912,  275.08609743]), 43: numpy.array([ 515.0599696 ,  275.08609743]), 
				44: numpy.array([ 139.09287797,  330.03091201]), 45: numpy.array([ 465.04004927 ,  330.030912018]), 
				46: numpy.array([ 160.05273126,  383.00691517]), 47: numpy.array([ 193.0564177,  377.00691517]), 48: numpy.array([ 233.07237285,  370.00691517]), 49: numpy.array([ 263.09216978,  365.00691517]), 50: numpy.array([ 300.03866965,  360.00691517 ]), 51: numpy.array([ 333.08349278 ,  365.00691517]), 52: numpy.array([ 370.04237352,  370.00691517]), 53: numpy.array([ 410.06692057,  377.00691517]), 54: numpy.array([443.01567001,  383.00691517]), 
				55: numpy.array([ 200.09722856,  420.00092204]), 56: numpy.array([ 240.00722902,  407.00439586]), 57: numpy.array([ 300.03866965,  410.04843548]), 58: numpy.array([ 360.07697474,  407.05637171]), 59: numpy.array([ 400.00957876,  420.00092204]),
				60: numpy.array([ 250.00722902 ,  448.07071622]), 61: numpy.array([ 300.03866965,  455.00095066]), 62: numpy.array([ 350.05840647,  448.07197886]), 
				63: numpy.array([ 300.03866965,  500.08420475])}#, 64: numpy.array([ 0.06108541,  0.06567389]), 65: numpy.array([ 0.05960185,  0.0956992 ]), 66: numpy.array([ 0.03633343,  0.05853592]), 67: numpy.array([ 0.07743313,  0.04829051]), 68: numpy.array([ 0.        ,  0.05866004]), 69: numpy.array([ 0.09708561,  0.04884912]), 70: numpy.array([ 0.01750468,  0.0312812 ]), 71: numpy.array([ 0.1      ,  0.0341625]), 72: numpy.array([ 0.07889184,  0.05353793]), 73: numpy.array([ 0.05978063,  0.07012536]), 74: numpy.array([ 0.01241063,  0.03331976]), 75: numpy.array([ 0.05342753,  0.09436357]), 76: numpy.array([ 0.05876311,  0.06644972]), 77: numpy.array([ 0.02750838,  0.01507112]), 78: numpy.array([ 0.01385156,  0.06392398]), 79: numpy.array([ 0.06621961,  0.00647077]), 80: numpy.array([ 0.01287236,  0.03147086]), 81: numpy.array([ 0.02336518,  0.07948883]), 82: numpy.array([ 0.00953532,  0.03230657]), 83: numpy.array([ 0.01804648,  0.08990819]), 84: numpy.array([ 0.08058014,  0.0904769 ]), 85: numpy.array([ 0.003309  ,  0.06884944]), 86: numpy.array([ 0.00950546,  0.07820378]), 87: numpy.array([ 0.07683669,  0.00485011]), 88: numpy.array([ 0.07270306,  0.02099295]), 89: numpy.array([ 0.08184965,  0.01078525]), 90: numpy.array([ 0.0075755 ,  0.01805681]), 91: numpy.array([ 0.00072032,  0.03368326]), 92: numpy.array([ 0.02174963,  0.01079548]), 93: numpy.array([ 0.07910862,  0.02134963]), 94: numpy.array([ 0.01228009,  0.06331738]), 95: numpy.array([ 0.0746584 ,  0.02159275]), 96: numpy.array([ 0.05927043,  0.07378723]), 97: numpy.array([ 0.01025312,  0.03471603]), 98: numpy.array([ 0.0722573 ,  0.04345764]), 99: numpy.array([ 0.08054124,  0.01462422]),99: numpy.array([ 0.08054124,  0.01462422])}  
			#with writer.saving(fig, "%s/Network_Reconstructed_XCORR_PHASE_LAG_Coexistence_Thresh_%s_%s.mpg" %(path_network,thresh,state), 150):
		
			G=nx.from_numpy_matrix(Adj_Matrix)	
		
			nx.set_node_attributes(G,'pos',position)
			labels={}
			for i in range(0,nNodes):
				labels[i] = Net_labels[1][i]
			#a=nx.draw_networkx_edges(G,position)
			ax1=plt.gca()
			#ax1.legend([a,b,c,d],['Complete synchronization','Lag synchronization','Phase synchronization','Generalized synchronization'], frameon=False,loc='lower right',prop={'size':65})
			ax1.set_frame_on(False)
			ax1.set_xticks([])
			ax1.set_yticks([])
			ax1.set_xticklabels([])
			State_indicator = ax_1.annotate('State: %s' %state,xy=(1,1))
			a=nx.draw_networkx_edges(G,position,edgelist=list(List_edges_Comp),alpha=0.5, width=3.0,edge_color='#DAA520',style='solid', label="Complete synchronization")
			b=nx.draw_networkx_edges(G,position,edgelist=list(List_edges_Lag),alpha=0.5,width=3.0,edge_color='#00FF00',style='solid',label="Lag synchronization")
			c=nx.draw_networkx_edges(G,position,edgelist=list(List_edges_Phase),alpha=0.5,width=3.0,edge_color='#C71585',style='solid',label="Phase synchronization")
			writer.grab_frame()
			a.remove()
			b.remove()
			c.remove()
			State_indicator.remove()
			
			#plt.close()
			
