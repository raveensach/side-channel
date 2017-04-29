'''This is the temporal feature extraction for the acoustic channel'''
import sys
sys.path.append('..')
from pymir import Onsets, Frame
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
from scipy.stats import iqr, skew, kurtosis
# from scipy.stats import skew
# from scipy.stats import kurtosis


class AcousticTemporal(object):
    ''' Get the Acoustic Temporal Features for the wav file'''

    def __init__(self):
        self.features = []

    def get_features(self, fixedframe):
        '''get all features '''
        self.features.append(self.mean(fixedframe))
        self.features.append(self.median(fixedframe))
        self.features.append(self.standard_dev(fixedframe))
        self.features.append(self.variance(fixedframe))
        self.features.append(self.iqr(fixedframe))
        # self.features.append(self.zcr(fixedframe))
        self.features.append(self.skewness(fixedframe))
        self.features.append(self.kurtosis(fixedframe))
        return self.features


    def mean(self, fixedframe):
        '''Mean features for the frame'''
        mean = []
        for frame in fixedframe:
            mean.append(np.mean(frame))
        return mean

    def median(self, fixedframe):
        '''meadian features for each frame'''
        median = []
        for frame in fixedframe:
            median.append(np.median(frame))
        return median

    def standard_dev(self, fixedframe):
        '''meadian for each frame'''
        stdd = []
        for frame in fixedframe:
            stdd.append(np.std(frame))
        return stdd

    def variance(self, fixedframe):
        ''' variance in each frame'''
        var = []
        for frame in fixedframe:
            var.append(np.var(frame))
        return var

    def iqr(self, fixedframe):
        '''Inter quatile range '''
        iqrange = []
        for frame in fixedframe:
            iqrange.append(iqr(frame))
        return iqrange

    # error: unbound method zcr() must be called with Frame instance
    #  as first argument (got ndarray instance instead) : Raveen
    def zcr(self, fixedframe):
        '''zero crossing range'''
        zcrange = []
        for frame in fixedframe:
            zcrange.append(Frame.zcr(frame))
        return zcrange

    def skewness(self, fixedframe):
        '''skewness for each frame'''
        skness = []
        for frame in fixedframe:
            skness.append(skew(frame))
        return skness

    def kurtosis(self, fixedframe):
        '''kurtosis for each frame'''
        kurt = []
        for frame in fixedframe:
            kurt.append(kurtosis(frame))
        return kurt
