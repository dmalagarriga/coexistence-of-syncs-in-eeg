import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy
import scipy
import os
import pylab
import networkx as nx
import sys
pylab.ion()
from tqdm import tqdm # this is the progress bar

########################
# Computes which pairs are highly cross 
# correlated and highly PLV (Phase Locking Value) 
# correlated and generalized sync
########################

path=os.getenv('P_Dir')

nNodes=64


# Threshold to apply (not its number but which is it)

thresh=int(os.getenv('Threshold'))
Condition_Xcorr_Complete_and_Delay=float(os.getenv('Thresh_XCORR'))
Condition_Delay_Gen_Sync=1.0 #Condition for Generalized synchronization. Not applicable it seems.
Condition_Phase_Sync_Xcorr=0.7 # Condition for not sync pairs (lower bound)--> anything lower than this is considered not sync
Condition_Phase_Sync_PLV=float(os.getenv('Thresh_PLV'))



C = numpy.genfromtxt('%s/Correlation_Sorted_By_Pairs_Filtered.dat' %(path),dtype=(int,int,float,float))
D = numpy.genfromtxt('%s/PLV_sync.dat' %(path),dtype=(int,int,float))
#C = numpy.genfromtxt('%s/Correlation_Sorted_By_Pairs.dat' %(path),dtype=(tuple,tuple,float,float))
#C = numpy.loadtxt('%s/Correlation_Sorted_By_Pairs.dat' %(path), unpack=True)

fout=open('%s/Only_Not_sync_pairs_XCORR_PHASE_LAG_Thresh_%s.dat' %(path,thresh),'w')
fout2=open('%s/Only_Generalized_sync_pairs_XCORR_PHASE_LAG_Thresh_%s.dat' %(path,thresh),'w')
fout3=open('%s/Only_Complete_sync_pairs_XCORR_PHASE_LAG_Thresh_%s.dat'%(path,thresh),'w')
fout4=open('%s/Only_Lag_sync_pairs_XCORR_PHASE_LAG_Thresh_%s.dat' %(path,thresh),'w')
fout5=open('%s/Only_Phase_sync_pairs_XCORR_PHASE_LAG_Thresh_%s.dat' %(path,thresh),'w')
Threshold=open('%s/Threshold_%s.dat' %(path,thresh),'w')


Complete_Sync_Pairs=[] 
PLV_Sync_Pairs=[] 
Lag_Sync_Pairs=[] 
Not_Sync_Pairs=[] 
Generalized_Sync_Pairs=[] 
Hist=[]

for j in tqdm(range(len(C))):
	if(C[j][3]==0.0):
		if(float(C[j][2]) >float(Condition_Xcorr_Complete_and_Delay)):
			Complete_Sync_Pairs.append((C[j][0],C[j][1]))
			Hist.append(1)
		#else:
		#	Not_Sync_Pairs.append((C[j][0],C[j][1]))
			
	elif(C[j][3]!=0.0):
		if(abs(float(C[j][3]))>float(Condition_Delay_Gen_Sync) and float(C[j][2]) > float(Condition_Xcorr_Complete_and_Delay) ):
			Generalized_Sync_Pairs.append((C[j][0],C[j][1]))
			Hist.append(4)
		if(abs(float(C[j][3]))<float(Condition_Delay_Gen_Sync) and float(C[j][2]) > float(Condition_Xcorr_Complete_and_Delay)):
			Lag_Sync_Pairs.append((C[j][0],C[j][1]))
			Hist.append(3) 
						
for j in range(len(D)):
	for k in range(len(C)):
		if((D[j][0],D[j][1])==(C[k][0],C[k][1]) or (D[j][1],D[j][0])==(C[k][1],C[k][0])):
			if(float(D[j][2])>float(Condition_Phase_Sync_PLV)):# and float(C[k][2])< float(Condition_Phase_Sync_Xcorr)):
				if (float(D[j][2])>float(C[k][2])):
					PLV_Sync_Pairs.append((D[j][0],D[j][1]))
					Hist.append(2)
			elif(float(D[j][2])<float(Condition_Phase_Sync_PLV) and float(C[k][2])<float(Condition_Phase_Sync_Xcorr)):
				Not_Sync_Pairs.append((D[j][0],D[j][1]))
				Hist.append(0)

print("Thresh Complete: Xcorr>%s" %Condition_Xcorr_Complete_and_Delay,"Thresh Gen: XCorr> %s, Delay>1.0" %Condition_Xcorr_Complete_and_Delay,
"Thresh Lag: XCorr> %s, Delay<1.0" %Condition_Xcorr_Complete_and_Delay, "Thresh Phase: PLV> %s, XCorr<%s" %(Condition_Phase_Sync_PLV,Condition_Phase_Sync_Xcorr),
file=Threshold)

print('Writing to file...\n')
for i,j in Not_Sync_Pairs:
	print(i,j,file=fout)
	
for i,j in Generalized_Sync_Pairs:
	print(i,j,file=fout2)

for i,j in Complete_Sync_Pairs:
	print(i,j,file=fout3)

for i,j in Lag_Sync_Pairs:
	print(i,j,file=fout4)

for i,j in PLV_Sync_Pairs:
	print(i,j,file=fout5)
	
				

