import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
import argparse 
from scipy import fftpack
import time

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=False, default='filename.wav')
args = parser.parse_args()

print("drawing plot for", args.filename)

samplerate, data = sio.wavfile.read(args.filename)
fftsize = len(data)
start_time = time.time()
data_fft = fftpack.fft(data, fftsize)
elapsed_time = time.time() - start_time

print("FFT 시간:", elapsed_time, "초")

# fast fourier transform 
