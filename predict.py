from IPython.display import display
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt


folder ='MDataFiles_Stage1'

Seeds = pd.read_csv(folder + '/' + 'MNCAATourneySeeds.csv')

display(Seeds)
