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

fixedFrames = wavData.frames(8830)
windowFunction=np.hamming
fixedFrames=wavData.frames(8830,windowFunction)

skness=[]
for frame in fixedFrames:
	skness.append(skew(frame))

print(len(skness))
#featurezcr=np.asarray(fixedFrames)


np.savetxt("skewness.csv", skness, delimiter=",")

print(type(fixedFrames))
print(len(fixedFrames))