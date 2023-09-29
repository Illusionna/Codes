import os
import time
import random
import shutil
import platform
import numpy as np
import pandas as pd
from tqdm import tqdm
from typing import List
from copy import deepcopy
from typing import Literal
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from sklearn.metrics import davies_bouldin_score
from sklearn.mixture import GaussianMixture as GMM
from sklearn.metrics.pairwise import pairwise_distances