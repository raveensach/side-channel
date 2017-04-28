import sys
#sys.path.append('C:/Users/Raveen/Desktop/pymir-master/pymir')
sys.path.append('..')

from pymir import AudioFile
from pymir import Energy
from pymir import Onsets

import matplotlib.pyplot as plt

import numpy as np

from pymir import Onsets
from scipy.signal import savgol_filter

wavData = AudioFile.open("Voice_005.wav")

fixedFrames = wavData.frames(8830)
windowFunction=np.hamming
fixedFrames=wavData.frames(8830,windowFunction)

fixedFrames=savgol_filter(fixedFrames,5,2)

zcrate=[]
for frame in fixedFrames:
	zcrate.append(frame.energy())

print(len(zcrate))
featurezcr=np.asarray(zcrate)
#np.savetxt("energy.csv", featurezcr, delimiter=",")

plt.plot(wavData)
plt.show()

print(type(fixedFrames))
print(len(fixedFrames))