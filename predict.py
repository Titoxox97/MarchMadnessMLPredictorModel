from IPython.display import display

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

folder ='data/MDatafiles_Stage0'

Seeds = pd.read_csv(folder+"MNCAATourneySeeds.csv")

display(Seeds)
