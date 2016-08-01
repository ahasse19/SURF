# Trying to make the error bars work


import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


i = 11
j = 50  

guessregress = [i, j]
    
def line(x, i, j):
    return i*x + j    


def barred():
    x = [662, 60, 1170, 1330, 511, 1274]
    y = [7425.6, 702.5, 13764.4, 15761.1, 5738.7, 14363.2]
    err = [368.3, 129.1, 790.3, 421, 325.4, 398.3]
    yfit = []
    linfit = curve_fit(line, x, y, guessregress, sigma = err)
    for i in range(1400):
        yfit.append(i*linfit[0][0] + linfit[0][1])
    plt.errorbar(x, y, yerr= err, linestyle = 'None', marker = 'o', label = 'Raw Data Points')
    plt.plot(range(1400), yfit, label = 'Line of Best Fit')
    plt.ylim(-100, 17000)
    plt.title('Channel to Kev Count for Four Radioactive Sources')
    plt.xlabel('KeV')
    plt.ylabel('Channels (ADC)')
    plt.legend(loc = 2)
    plt.show()
    print linfit[0][1]
 
       