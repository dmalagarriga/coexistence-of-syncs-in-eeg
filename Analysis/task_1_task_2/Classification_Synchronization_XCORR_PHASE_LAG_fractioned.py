import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy
import scipy
import os
import pylab
import networkx as nx
import sys
import glob
pylab.ion()

########################
# Computes which pairs are highly cross 
# correlated and highly PLV (Phase Locking Value) 
# correlated and generalized sync
########################

path=os.getenv('P_Dir')
Threshold=os.getenv('Threshold')
pairs=os.getenv('Pairs')
path_output = '%s/%s/Thresh_%s/' %(path,pairs,Threshold)
situation=os.getenv('situation')
subject = int(os.getenv('number'))
#K1=float(os.getenv('K1'))
#initial_nodes=int(os.getenv('Initial_Nodes'))
#Seed=int(os.getenv('Seed'))
nNodes=64


# Threshold to apply (not its number but which is it)

thresh=int(os.getenv('Threshold'))
Condition_Xcorr_Complete_and_Delay=float(os.getenv('Thresh_XCORR'))
Condition_Delay_Gen_Sync=1.0
Condition_Phase_Sync_Xcorr=0.9
Condition_Phase_Sync_PLV=float(os.getenv('Thresh_PLV'))

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

for k in range(len(Annotations)):
	time = numpy.genfromtxt(infiles[0],unpack=True,delimiter=',',usecols=0,skip_header=0)
	dt = time[1]-time[0]
	Range = (float(Annotations[k][0])/dt)+(float(Annotations[k][1])/dt)

	C = numpy.genfromtxt('%s/Correlation_%s_%s.dat' %(path,Annotations[k][0],Annotations[k][2]),dtype=(int,int,float,float))
	D = numpy.genfromtxt('%s/PLV_sync_%s_%s.dat' %(path,Annotations[k][0],Annotations[k][2]),dtype=(int,int,float))
	#C = numpy.numpy.genfromtxt('%s/Correlation_Sorted_By_Pairs.dat' %(path),dtype=(tuple,tuple,float,float))
	#C = numpy.loadtxt('%s/Correlation_Sorted_By_Pairs.dat' %(path), unpack=True)

	#fout=open('%s/Only_Not_sync_pairs_XCORR_PHASE_LAG_Thresh_%s_%s_%s.dat' %(path,thresh,Annotations[k][0],Annotations[k][2]),'w')
	#fout2=open('%s/Only_Generalized_sync_pairs_XCORR_PHASE_LAG_Thresh_%s_%s_%s.dat' %(path,thresh,Annotations[k][0],Annotations[k][2]),'w')
	fout3=open('%s/Only_Complete_sync_pairs_XCORR_PHASE_LAG_Thresh_%s_%s_%s.dat'%(path_output,thresh,Annotations[k][0],Annotations[k][2]),'w')
	fout4=open('%s/Only_Lag_sync_pairs_XCORR_PHASE_LAG_Thresh_%s_%s_%s.dat' %(path_output,thresh,Annotations[k][0],Annotations[k][2]),'w')
	fout5=open('%s/Only_Phase_sync_pairs_XCORR_PHASE_LAG_Thresh_%s_%s_%s.dat' %(path_output,thresh,Annotations[k][0],Annotations[k][2]),'w')
	Threshold=open('%s/Threshold_%s_%s_%s.dat' %(path_output,thresh,Annotations[k][0],Annotations[k][2]),'w')


	Complete_Sync_Pairs=[] 
	PLV_Sync_Pairs=[] 
	Lag_Sync_Pairs=[] 
	Not_Sync_Pairs=[] 
	Generalized_Sync_Pairs=[] 
	Hist=[]
	
	for j in range(len(C)):
		if(C[j][3]==0.0):
			if(float(C[j][2]) >float(Condition_Xcorr_Complete_and_Delay)):
				Complete_Sync_Pairs.append((C[j][0],C[j][1]))
				Hist.append(1)
			#else:
			#	Not_Sync_Pairs.append((C[j][0],C[j][1]))
			
		elif(C[j][3]!=0.0):
		#	if(abs(float(C[j][3]))>float(Condition_Delay_Gen_Sync) and float(C[j][2]) > float(Condition_Xcorr_Complete_and_Delay) ):
		#		Generalized_Sync_Pairs.append((C[j][0],C[j][1]))
		#		Hist.append(4)
			if(abs(float(C[j][3]))<float(Condition_Delay_Gen_Sync) and float(C[j][2]) > float(Condition_Xcorr_Complete_and_Delay)):
				Lag_Sync_Pairs.append((C[j][0],C[j][1]))
				Hist.append(3) 
	
	for j in range(len(D)):
		for k in range(len(C)):
			if((D[j][0],D[j][1])==(C[k][0],C[k][1]) or (D[j][1],D[j][0])==(C[k][1],C[k][0])):
				if float(D[j][2])>float(Condition_Phase_Sync_PLV) and float(C[k][2])<Condition_Phase_Sync_Xcorr:
					
					PLV_Sync_Pairs.append((D[j][0],D[j][1]))
					Hist.append(2)
		#		elif float(D[j][2])<float(Condition_Phase_Sync_PLV) and float(C[k][2]) <Condition_Phase_Sync_Xcorr:
		#			Not_Sync_Pairs.append((D[j][0],D[j][1]))
		#			Hist.append(0)
	

	print >> Threshold,"Thresh Complete: Xcorr>%s" %Condition_Xcorr_Complete_and_Delay,"Thresh Gen: XCorr> %s, Delay>1.0" %Condition_Xcorr_Complete_and_Delay,"Thresh Lag: XCorr> %s, Delay<1.0" %Condition_Xcorr_Complete_and_Delay, "Thresh Phase: PLV> %s, XCorr<%s" %(Condition_Phase_Sync_PLV,Condition_Phase_Sync_Xcorr)

	#for i,j in Not_Sync_Pairs:
	#	print >>fout,i,j
	#for i,j in Generalized_Sync_Pairs:
#		print >>fout2,i,j
	for i,j in Complete_Sync_Pairs:
		print >>fout3,i,j
	for i,j in Lag_Sync_Pairs:
		print >>fout4,i,j
	for i,j in PLV_Sync_Pairs:
		print >>fout5,i,j	
				

