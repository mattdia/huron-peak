# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:15:15 2016

@author: MattDay
"""
#Header ---------------------------
from numpy import pi, absolute, log1p
from scipy.signal import firwin, kaiserord, freqz
from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, axes, show

#----------------------------------

#Frequency Parameters -------------
sampleRate = 65

nyquist_freq = sampleRate/2

freq_width = 2/nyquist_freq

cutoff_freq = [10]
#----------------------------------

#Filter Peripherals ---------------
ripple_db = 40

num_taps, beta = kaiserord(ripple_db, freq_width)

filt_pass_zero = False

cut_unitless = [i/nyquist_freq for i in cutoff_freq]
#----------------------------------

#Tap Limiter ----------------------
if num_taps > 50:
    num_taps_lim = 50
else:
    num_taps_lim = num_taps
#----------------------------------

#Filter Generation-----------------

if num_taps_lim % 2 == 0 and filt_pass_zero == False:
    filt = firwin(num_taps_lim + 1, cut_unitless, pass_zero = filt_pass_zero)
else:
    filt = firwin(num_taps_lim, cut_unitless, pass_zero = filt_pass_zero)
    
#----------------------------------
    
#Filter Performance Model ---------

figure(2)
clf()
w, h = freqz(filt, worN=8000)
h2 = 0.5 * log1p(absolute(h))
plot((w/pi)* nyquist_freq, h2, linewidth=2)
xlabel('Frequency (MHz)')
ylabel('Gain')
title('Frequency Response')
ylim(-0.05, max(h2))
grid(True)

print("Number of Taps:", len(filt))
    
#----------------------------------