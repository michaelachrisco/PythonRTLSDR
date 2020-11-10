from rtlsdr import RtlSdr
import termplotlib as tpl
import numpy

# x = len(samples)
# y = []

sdr = RtlSdr()
# https://www.oreilly.com/library/view/elegant-scipy/9781491922927/ch04.html
# attempt to see waveform if possible TODO!

# configure device
sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = 101e6     # Hz
sdr.freq_correction = 60   # PPM
sdr.gain = 4
import numpy as np

# samples = sdr.read_samples(256*1024)
samples = sdr.read_samples(256)
x = range(len(samples))


# print(samples.real)
# i = 0
# for sample in samples[:3]:
#   x.append(i)
#   i=i+1
#   y.append(-1*sample.real)


fig = tpl.figure()
fig.plot(x, samples, label="data", width=180, height=512)
fig.show()



from pylab import *
from rtlsdr import *

# sdr = RtlSdr()

# configure device
# sdr.sample_rate = 2.4e6
# sdr.center_freq = 95e6
sdr.gain = 4

# samples = sdr.read_samples(256*1024)
sdr.close()
print(sdr.sample_rate/1e6)
# use matplotlib to estimate and plot the PSD
# This part works...
psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
xlabel('Frequency (MHz)')
ylabel('Relative power (dB)')
# print(max(samples))

show()

