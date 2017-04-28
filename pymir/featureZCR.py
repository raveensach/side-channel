import sys
#sys.path.append('C:/Users/Raveen/Desktop/pymir-master/pymir')
sys.path.append('..')

from pymir import AudioFile
from pymir import Energy
from pymir import Onsets
from pymir import Frame

import matplotlib.pyplot as plt

import numpy as np

from pymir import Onsets
from scipy.signal import savgol_filter

wavData = AudioFile.open("Voice_005.wav")

wavData=savgol_filter(wavData,17,1)

#fixedFrames = wavData.frames(8830)
fixedFrames=Frame.frames(wavData,8830)
#windowFunction=np.hamming
#fixedFrames=wavData.frames(8830,windowFunction)


zcrate=[]
for frame in fixedFrames:
	zcrate.append(Frame.zcr(frame))

print(len(zcrate))
featurezcr=np.asarray(zcrate)
#np.savetxt("energy.csv", featurezcr, delimiter=",")

plt.plot(zcrate)
plt.show()

print(type(fixedFrames))
print(len(fixedFrames))