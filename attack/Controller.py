'''
Get the wav file and magnetic file then output the feature vectors
'''
import sys
sys.path.append('..')
from pymir import AudioFile
from AcousticTemporal import AcousticTemporal
import matplotlib.pyplot as plt

import numpy as np
from scipy.signal import savgol_filter

# ACOUSTIC
WAVDATA = AudioFile.open("audiofiles/Voice_005.wav")

# savitzky golay filter

fixedFrames = WAVDATA.frames(8830)
windowFunction=np.hamming
fixedFrames=WAVDATA.frames(8830,windowFunction)

# find out if filter should come before fixed Frames? what are 5 and 2
# Check: https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.signal.savgol_filter.html
fixedFrames=savgol_filter(fixedFrames,5,2)

# Acoustic Temporal feature extraction
mag_temp = AcousticTemporal()
acoustic_features = mag_temp.get_features(fixedFrames)
print(acoustic_features)

# Acoustic Spectoral Feature extraction :Solomon

# MAGNETIC
# temporal features
# spectoral features