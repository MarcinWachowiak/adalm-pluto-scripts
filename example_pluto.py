#%%
import adi
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal, fft# Create radio
sdr = adi.Pluto()

#%%
# Configure properties
sample_rate = int(5e+6)
sdr.rx_rf_bandwidth = sample_rate
sdr.rx_lo = int(94.6e+6)
sdr.sample_rate = sample_rate
sdr.rx_buffer_size = 2**16
# Read properties
print("RX LO %s" % (sdr.rx_lo))

# Collect data
sig = sdr.rx()
sig = sdr.rx()
plt.plot(np.real(sig))
plt.plot(np.imag(sig))
plt.xlabel("Samples")
plt.ylabel("Amplitude [dbFS]")
plt.show()

#%%
w = signal.blackman(2**16)
fft_dat = fft.fft(w*sig)
plt.plot(fft_dat)
plt.show()

# %%
