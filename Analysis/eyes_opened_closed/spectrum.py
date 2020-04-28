from pylab import *
from numpy import *
from scipy import *
from scipy.signal import coherence
import sys
from matplotlib.mlab import psd

def PSD(t,data,PieceLength):
	dt =t[1]-t[0]
	pxx, freqs = psd( data, NFFT=PieceLength,pad_to=None, Fs=1./dt,scale_by_freq=True)
	return pxx, freqs

def peakdet(v, delta, x = None):
    """
Converted from MATLAB script at http://billauer.co.il/peakdet.html
Currently returns two lists of tuples, but maybe arrays would be better
function [maxtab, mintab]=peakdet(v, delta, x)
%PEAKDET Detect peaks in a vector
% [MAXTAB, MINTAB] = PEAKDET(V, DELTA) finds the local
% maxima and minima ("peaks") in the vector V.
% MAXTAB and MINTAB consists of two columns. Column 1
% contains indices in V, and column 2 the found values.
%
% With [MAXTAB, MINTAB] = PEAKDET(V, DELTA, X) the indices
% in MAXTAB and MINTAB are replaced with the corresponding
% X-values.
%
% A point is considered a maximum peak if it has the maximal
% value, and was preceded (to the left) by a value lower by
% DELTA.
% Eli Billauer, 3.4.05 (Explicitly not copyrighted).
% This function is released to the public domain; Any use is allowed.
"""
    maxtab = []
    mintab = []
       
    if x is None:
        x = arange(len(v))
    
    v = asarray(v)
    
    if len(v) != len(x):
        sys.exit('Input vectors v and x must have same length')
    
    if not isscalar(delta):
        sys.exit('Input argument delta must be a scalar')
    
    if delta <= 0:
        sys.exit('Input argument delta must be positive')
    
    mn, mx = Inf, -Inf
    mnpos, mxpos = NaN, NaN
    
    lookformax = True
    
    for i in arange(len(v)):
        this = v[i]
        if this > mx:
            mx = this
            mxpos = x[i]
        if this < mn:
            mn = this
            mnpos = x[i]
        
        if lookformax:
            if this < mx-delta:
                maxtab.append((mxpos, mx))
                mn = this
                mnpos = x[i]
                lookformax = False
        else:
            if this > mn+delta:
                mintab.append((mnpos, mn))
                mx = this
                mxpos = x[i]
                lookformax = True

    return maxtab, mintab
    	
#if __name__=="__main__":
#    series = [0,0,0,2,0,0,0,-2,0,0,0,2,0,0,0,-2,0]
#    print peakdet(series,1)

def average(values):

	return sum(values, 0.0)/len(values)
	
	
def coherence(t,data1,data2):
	dt =(t[1]-t[0])
	
	cxy, f = cohere(data1,data2, int(256.0/5), Fs=1./dt,detrend='none',
	window=mlab.window_hanning, noverlap=0, pad_to=None,
    sides='default',scale_by_freq=None)
	return cxy, f

def cross_spectral_density(t,data1,data2):
	dt = (t[1]-t[0])
	pxy, f = csd(data1,data2,16384, Fs=1./dt, detrend=mlab.detrend_none,
    window=mlab.window_hanning, noverlap=0, pad_to=None,
    sides='default', scale_by_freq=True)
	return pxy, f	

def normalized_cross_spectral_density(t,x, y, NFFT=256, Fs=1./0.0058, detrend=detrend_linear, window=window_hanning, noverlap=0,scale_by_freq=True):
    """
    cohere the coherence between x and y.  Coherence is the normalized
    cross spectral density

    Cxy = |Pxy|^2/(Pxx*Pyy)

    The return value is (Cxy, f), where f are the frequencies of the
    coherence vector.  See the docs for psd and csd for information
    about the function arguments NFFT, detrend, windowm noverlap, as
    well as the methods used to compute Pxy, Pxx and Pyy.

    """
	
    dt = (t[1]-t[0])
    
    Pxx,f = psd(x, NFFT=NFFT, Fs=1./dt, detrend=detrend,window=window, noverlap=noverlap,scale_by_freq=True)
    Pyy,f = psd(y, NFFT=NFFT, Fs=1./dt, detrend=detrend,window=window, noverlap=noverlap,scale_by_freq=True)
    Pxy,f = csd(x, y, NFFT=NFFT, Fs=1./dt, detrend=detrend,window=window, noverlap=noverlap,scale_by_freq=True)

    
    Cxy = divide(absolute(Pxy)**2, Pxx*Pyy)
    
    return Cxy, f
