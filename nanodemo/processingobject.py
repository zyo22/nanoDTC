import os
import sys
import pandas as pd
import scipy.optimize as so
import matplotlib.pyplot as plt
from collections import defaultdict
import scipy.ndimage as gauss_filter

from nanodemo.functions import *
from nanodemo.dataobject import DataObject
from nanodemo.models import hertz_model


class ProcessingObject():

    def __init__(self, path_to_file_or_list_of_files):
        pass

    def _preprocessing(self):
        pass

    def fit_models(self):
        pass

    def to_csv(self):
        pass


if __name__ == "__main__":
    pass
