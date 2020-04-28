import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy 
import scipy
import os
import pylab
import networkx as nx
import sys
from os.path import join as pjoin
import warnings
from tqdm import tqdm # this is the progress bar


pylab.ion()

#OPTIONS
plot_matrices= 0
plot_network=1
compute_matrices=1
nNodes=64

thresh=int(os.getenv('Threshold'))
path=os.getenv('P_Dir')
situation=os.getenv('situation')
subject = int(os.getenv('number'))
sync_patterns_folder=os.getenv('Sync_patterns')


if situation == 'Eyes_opened':	
	Net_labels =  numpy.loadtxt('%s/S%03iR01_signals.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1),dtype=('|S4','|S4'), skiprows=1)
if situation == 'Eyes_closed':
	Net_labels =  numpy.loadtxt('%s/S%03iR02_signals.txt' %(path,subject),unpack=True,delimiter=',', usecols = (0,1),dtype=('|S4','|S4'), skiprows=1)
if (compute_matrices==1):
	
	# Phase and correlation of every node
	Xcorr = numpy.genfromtxt('%s/Correlation_Sorted_By_Pairs_Filtered.dat' %(path),dtype=(int,int,float,float))
	Phase = numpy.genfromtxt('%s/PLV_sync.dat' %(path),dtype=(int,int,float))
	
	# Classified pairs
	with warnings.catch_warnings():
		warnings.simplefilter("ignore")
		Not_Sync = numpy.genfromtxt('%s/Only_Not_sync_pairs_XCORR_PHASE_LAG_Thresh_%s.dat' %(path,thresh),dtype=(int,int))
		Complete_Sync = numpy.genfromtxt('%s/Only_Complete_sync_pairs_XCORR_PHASE_LAG_Thresh_%s.dat' %(path,thresh),dtype=(int,int))
		Lag_Sync = numpy.genfromtxt('%s/Only_Lag_sync_pairs_XCORR_PHASE_LAG_Thresh_%s.dat' %(path,thresh),dtype=(int,int))
		Phase_Sync = numpy.genfromtxt('%s/Only_Phase_sync_pairs_XCORR_PHASE_LAG_Thresh_%s.dat' %(path,thresh),dtype=(int,int))
		Gen_Syn = numpy.genfromtxt('%s/Only_Generalized_sync_pairs_XCORR_PHASE_LAG_Thresh_%s.dat' %(path,thresh),dtype=(int,int))

	'''
	Not_Sync = numpy.loadtxt('%s/Not_sync_pairs.dat' %(path),unpack=True)
	Complete_Sync = numpy.loadtxt('%s/Complete_sync_pairs.dat' %(path),unpack=True)
	Lag_Sync = numpy.loadtxt('%s/Lag_sync_pairs.dat' %(path),unpack=True)
	Phase_Sync = numpy.loadtxt('%s/Phase_sync_pairs.dat' %(path),unpack=True)
	Gen_Syn = numpy.loadtxt('%s/Not_Connected_Generalized_sync_pairs.dat' %(path),unpack=True)
	'''
	Complete_Sync=Complete_Sync-1
	Not_Sync=Not_Sync-1
	Lag_Sync=Lag_Sync-1
	Phase_Sync=Phase_Sync-1
	Gen_Syn=Gen_Syn-1

	Corr_matrix= numpy.zeros([nNodes,nNodes])
	Delay_matrix= numpy.zeros([nNodes,nNodes])
	Phase_matrix = numpy.zeros([nNodes,nNodes])
	
	Adj_Complete_Sync=numpy.zeros([nNodes,nNodes])
	Adj_Lag_Sync=numpy.zeros([nNodes,nNodes])
	Adj_Phase_Sync=numpy.zeros([nNodes,nNodes])
	Adjacency_Matrix=numpy.zeros([nNodes,nNodes])

	#for i in range(len(Not_Sync)):
	#	Adjacency_Matrix[Not_Sync[i][0],Not_Sync[i][1]]=1
	#	Adj_Not_Sync=[Not_Sync[i][0],Not_Sync[i][1]]=1


	for i in tqdm(range(len(Xcorr))):
		Corr_matrix[Xcorr[i][0]-1,Xcorr[i][1]-1] = Xcorr[i][2] # -1 because python counts from 0 and I count from 1
		Delay_matrix[Xcorr[i][0]-1,Xcorr[i][1]-1] = abs(Xcorr[i][3])

	for i in range(len(Phase)):
		Phase_matrix[Phase[i][0]-1,Phase[i][1]-1] = Phase[i][2]
	
	for i in range(len(Complete_Sync)):
		Adjacency_Matrix[Complete_Sync[i][0],Complete_Sync[i][1]]=1
		Adjacency_Matrix[Complete_Sync[i][1],Complete_Sync[i][0]]=1
		Adj_Complete_Sync[Complete_Sync[i][0],Complete_Sync[i][1]-1]=1
	for i in range(len(Lag_Sync)):
		Adjacency_Matrix[Lag_Sync[i][0],Lag_Sync[i][1]] = 1
		Adjacency_Matrix[Lag_Sync[i][1],Lag_Sync[i][0]] = 1	
		Adj_Lag_Sync[Lag_Sync[i][0],Lag_Sync[i][1]] = 1

	if len(Phase_Sync) == 2:

		Adjacency_Matrix[Phase_Sync[0],Phase_Sync[1]] = 1
		Adjacency_Matrix[Phase_Sync[1],Phase_Sync[0]] = 1
		Adj_Phase_Sync[Phase_Sync[0],Phase_Sync[1]] = 1
	else:	
		for i in range(len(Phase_Sync)):
			Adjacency_Matrix[Phase_Sync[i][0],Phase_Sync[i][1]] = 1
			Adjacency_Matrix[Phase_Sync[i][1],Phase_Sync[i][0]] = 1
			Adj_Phase_Sync[Phase_Sync[i][0],Phase_Sync[i][1]] = 1
	for i in range(len(Gen_Syn)):
		if(len(Gen_Syn)==2):
			Adjacency_Matrix[Gen_Syn[0],Gen_Syn[1]] = 1
			Adjacency_Matrix[Gen_Syn[1],Gen_Syn[0]] = 1
		else:
			Adjacency_Matrix[Gen_Syn[i][0],Gen_Syn[i][1]] = 1
			Adjacency_Matrix[Gen_Syn[i][1],Gen_Syn[i][0]] = 1


if(plot_matrices==1):
	ax = plt.subplot() # Jjust creates a plot
	for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    		#label.set_fontname('Helvetica')
    		label.set_fontsize(30)
	axis_font = {'size':'30'}
	plt.pcolor(Delay_matrix,cmap='gnuplot',linewidth=0)	
	plt.xlim([0,nNodes])
	plt.ylim([0,nNodes])
	plt.title('Delay');plt.xlabel('Oscillator i', **axis_font);plt.ylabel('Oscillator j', **axis_font)
	plt.cbar=plt.colorbar()	
	plt.cbar.ax.set_ylabel('Delay')
	plt.savefig(pjoin(path,'Delay_Matrix_K_%s.eps' %(K1)))
	plt.close()
	
	plt.pcolor(Corr_matrix,cmap='gnuplot',linewidth=0)
	plt.xlim([0,nNodes])
	plt.ylim([0,nNodes])
	plt.title('Correlation matrix');plt.xlabel('Oscillator i', **axis_font);plt.ylabel('Oscillator j', **axis_font)
	plt.cbar=plt.colorbar(ticks=[0.0, 0.5, 1.0])
	plt.cbar.ax.set_ylabel('Correlation coefficient')
	plt.clim=([0.0,1.0])
	plt.savefig(pjoin(path,'Correlation_Matrix_K_%s.eps' %(K1)))
	plt.close()

	plt.pcolor(Phase_matrix,cmap='gnuplot', linewidth=0)
	plt.xlim([0,nNodes])
	plt.ylim([0,nNodes])
	plt.title('PLV matrix');plt.xlabel('Oscillator i', **axis_font);plt.ylabel('Oscillator j', **axis_font)
	plt.cbar=plt.colorbar(ticks=[0.0, 0.5, 1.0])
	plt.cbar.ax.set_ylabel('PLV')
	plt.clim=([0.0,1.0])
	plt.savefig(pjoin(path,'PLV_Matrix_K_%s.eps' %(K1)))
	plt.close()
if (plot_network==1):

	print('Ploting images \n')

	plt.figure(num=None,figsize=(10,10))
	img = mpimg.imread('Head_images/64_channel_sharbrough.png')
	#plt.axes([0.08, 0.08, 0.94-0.08, 0.94-0.08])
	implot = plt.imshow(img)
	G=nx.from_numpy_matrix(Adjacency_Matrix)	
	#G=nx.Graph()
	#H=nx.path_graph(64)
	#G.add_nodes_from(H)
	# NODE POSITION
	#path_network=os.getenv('P_Net')
	#Graph = nx.read_pajek('%s/Scale_Free_C_0.net' %path_network)

	#position={}
	#identity={}
	#for i in range(nNodes):
		#value=str(Graph.node['%i' %i]['id']).strip("'")
		#identity.update()
		#position.update({int(value)-1: numpy.numpy.array([Graph.node['%i' %i]['x'],Graph.node['%i' %i]['y']])})
	#	position.update({i: numpy.numpy.array([Graph.node['%i' %i]['x'],Graph.node['%i' %i]['y']])})

	
	#position = nx.spring_layout(G,scale=0.1)
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
	nx.set_node_attributes(G,position,'pos')
	labels={}
	for i in range(0,nNodes):
		labels[i] = Net_labels[1][i]
	
	'''
	for i in range(len(nx.strongly_connected_components(G))):
		if len(nx.connected_component_subgraphs(G)[i])>=2:
			nx.draw_networkx_nodes(nx.connected_component_subgraphs(G)[i],pos=position, node_color='gray',node_size=400,with_labels=True)
	for i in range(len(nx.strongly_connected_components(G))):
		if len(nx.connected_component_subgraphs(G)[i])>=2:
			nx.draw_networkx_labels(nx.connected_component_subgraphs(G)[i],position,labels,font_size=15)
	'''		
	
	#a=nx.draw_networkx_edges(G,position)
	ax1=plt.gca()
	#ax1.legend([a,b,c,d],['Complete synchronization','Lag synchronization','Phase synchronization','Generalized synchronization'], frameon=False,loc='lower right',prop={'size':65})
	ax1.set_frame_on(False)
	ax1.set_xticks([])
	ax1.set_yticks([])
	ax1.set_xticklabels([])
	a=nx.draw_networkx_edges(G,position,edgelist=list(Complete_Sync),alpha=0.5, width=3.0,edge_color='#DAA520',style='solid', 	label="Complete synchronization")
	b=nx.draw_networkx_edges(G,position,edgelist=list(Lag_Sync),alpha=0.5,width=3.0,edge_color='#00FF00',style='solid',label="Lag synchronization")
	c=nx.draw_networkx_edges(G,position,edgelist=list(Phase_Sync),alpha=0.5,width=3.0,edge_color='#C71585',style='solid',label="Phase synchronization")
	plt.legend()	

	
	#a=nx.draw_networkx_edges(G,position,edgelist=list(Complete_Sync),alpha=0.5, width=5.0,edge_color='#DAA520',style='solid', 	label="Complete synchronization")
	#d=nx.draw_networkx_edges(G,position,edgelist=list(Gen_Syn),alpha=0.5,width=5.0,edge_color='#0000FF',style='solid',label="Generalized synchronization")
	#e=nx.draw_networkx_edges(G,position,edgelist=list(Not_Sync),width=0.01,edge_color='#7F7F7F',style='solid',alpha=0.1,label="No synchronization")
	#c=nx.draw_networkx_edges(G,position,edgelist=list(Phase_Sync),alpha=0.5,width=5.0,edge_color='#C71585',style='solid',label="Phase synchronization")
	#b=nx.draw_networkx_edges(G,position,edgelist=list(Lag_Sync),alpha=0.5,width=5.0,edge_color='#00FF00',style='solid',label="Lag synchronization")

	pylab.savefig('%s/Network_Reconstructed_XCORR_PHASE_LAG_Thresh_%s.png' %(sync_patterns_folder,thresh),bbox_inches='tight')
	pylab.close()
	#numpy.savetxt(pjoin(path,'Adjacency_Matrix_from_Not_Connected_Nodes.dat'),Adjacency_Matrix)
	#nx.write_dot(G, '%s/Network_%06.3f_From_Not_Connected_5.dot' %(path,K1))
	#nx.write_gml(G, '%s/Network_%06.3f_From_Not_Connected_5.gml' %(path,K1))


