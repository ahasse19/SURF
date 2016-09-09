
# These are all of the libraries used in every program for the SURF purpose. Copy and paste into each file. 

%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.integrate as integrate
from scipy.optimize import minimize 
from scipy import stats
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy import interp


# Bestfit point from wikipedia method on line-line article

4800point = {{3.4517}, {9.36388}}
5500point = {{3.38845}, {8.66285}}
6000point = {{3.28793}, {8.16079}}
7700point = {{3.05644}, {7.94513}}

4800err = {1.36287, 0.0290772}
5500err = {1.31089, 0.0310162}
6000err = {1.2333, 0.0319127}
7700err = {1.10977, 0.0313639}

'''\setlength{\parskip}{2em}
\noindent
\section{Bibliography}

\noindent
Birks, J.B. (1964). The Theory and Practice of Scintillation Counting. London:
Pergamon.

\noindent
Polischuk, O., Belli, P., Bernabei, R., Capella, F., Caracciolo, V., Cerulli, R., . . . Tretyak, V. (2009). Radioactive contamination of BaF2 crystal scintillator. Nuclear Institute.
'''
