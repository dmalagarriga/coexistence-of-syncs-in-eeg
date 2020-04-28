from scipy.signal import butter, lfilter
import numpy as np
import os
import spectrum
import glob
from os.path import join as pjoin

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz
    nTrans=0
    # Path
    path=os.getenv('P_Dir')
    # Sample rate and desired cutoff frequencies (in Hz).
    fs = 173.61
    lowcut = 3.0
    highcut = 40.0

    # Plot the frequency response for a few different orders.
    '''
    plt.figure(1)
    plt.clf()
    for order in [3, 6, 9]:
        b, a = butter_bandpass(lowcut, highcut, fs, order=order)
        w, h = freqz(b, a, worN=2000)
        plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)

    plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
             '--', label='sqrt(0.5)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain')
    plt.grid(True)
    plt.legend(loc='best')
    '''
    
    # Filter a noisy signal.
    T = 23.6
    nsamples = T * fs
    t = np.linspace(0, T, nsamples, endpoint=True)
    
	# Signal data
    infiles = sorted(glob.glob( '%s/Z*.txt' %path))
    fout=open('%s/All_filtered_Z.dat' %path,'w')
    fout2 = open('%s/All_filtered_Z_peak_frequencies.dat' %path,'w')
    data_array=np.zeros([len(infiles)+1,nsamples])
    data_array[0] = t
    for i in range(len(infiles)):
    	data = np.loadtxt(infiles[i], unpack=True)

    	y = butter_bandpass_filter(data, lowcut, highcut, fs, order=7)
    	data_array[i+1] = y
    	(pxx,freqs)=spectrum.PSD(t[nTrans:], y[nTrans:]-y[nTrans:].mean(),16384)
    	MAXTAB1 = list(pxx)
    	MAX1= MAXTAB1.index(max(MAXTAB1))
    	#xs,ys =freqs[MAX1],max(MAXTAB1)
    	print >> fout2,i+1, freqs[MAX1],max(MAXTAB1)
    np.savetxt(pjoin(path,'All_filtered_Z.dat'),zip(*data_array),fmt='%06.4f',delimiter=' ')
    #for i in range(len(data_array)):
    #	for j in range(i):
    #		print>>fout, data_array[i,j],
    
    '''
    plt.figure(2)
    plt.clf()
    plt.plot(t, data, label='Noisy signal')
	
    plt.plot(t, y, label='Filtered signal')
    plt.xlabel('time (seconds)')
    #plt.hlines([-a, a], 0, T, linestyles='--')
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')
    
    plt.show()
    '''
    
    #plt.yscale('log')
    #plt.show()
    #plt.xlim([0, 40])
    #ax = plt.gca()

    #ax.annotate('%.3f' %(freqs[MAX1]),xy=(freqs[MAX1],max(MAXTAB1)))
    #plt.plot(xs,ys,marker='o')
    #plt.show()
	
