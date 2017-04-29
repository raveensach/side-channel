import sys
#sys.path.append('C:/Users/Raveen/Desktop/pymir-master/pymir')
sys.path.append('..')

from pymir import AudioFile
from pymir import Energy
from pymir import Onsets

import matplotlib.pyplot as plt

import numpy as np

from pymir import Onsets
from scipy.stats import skew

wavData = AudioFile.open("Voice_005.wav")

fixedFrames = wavData.frames(8824)
windowFunction=np.hamming
fixedFrames=wavData.frames(8830,windowFunction)

vr=[]
for frame in fixedFrames:
	vr.append(np.var(frame))

print(len(vr))
#featurezcr=np.asarray(fixedFrames)


np.savetxt("variance.csv", vr, delimiter=",")

print(type(fixedFrames))
print(len(fixedFrames))

