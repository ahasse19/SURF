# SURF Calibration and Quenching Factor for BaF2 General Program. (This version currently uses the first UV data)
# All functions are made to be general (user input for agruments; not users altering code values), however it is structured for 
# the ease of use for my SURF progject

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize 
from scipy import stats
from scipy.optimize import curve_fit
import math


    
def alldata(file):
    '''This function takes data from a file and outputs the columns into two lists. 
    The file must have two columns of data seperated by a tab'''
    point = []
    num = ''
    first = ''
    second = ''
    x = []
    y = []
    f = open(file, 'r')
    f.readline()
    for line in f:
        num = ''
        point = list(line)
        for i in range(len(point)):
            if point[0] == '\t':
                del point[0]
                first = num
                break
            else: 
                num += point[0]
                del point[0]
        num = ''
        for i in range(len(point)):
            if point[0] == '\t':
                del point[0]
                second = num
                break
            else: 
                num += point[0]
                del point[0]
        x.append(float(first))
        y.append(float(second))
    return x, y
    
def alldata2(file):
    '''Takes a text file and categorizes the data into two arrays based off of
    columns. Outputs two arrays, one for x and one for y'''
    data = np.genfromtxt(file)
    x = data[0]
    y = data[1]
    return x, y
    
    
def energy(x, y, upper, lower):
    ''' This function takes two lists and two integers and outputs two lists
    within the integer bounds. The bounds are determined by the x variable''' 
    g = 0
    newx = []
    newy = []
    for i in range(len(x)):
        if x[g] > lower:
                if x[g] < upper:
                    newx.append(x[g])
                    newy.append(y[g])
        g += 1
    return newx, newy
    

def rawdata(x, y, title, xname, yname, legend):
    ''' This function takes two lists and graphing information and plots the 
    lists against eachother'''
    plt.plot(x, y, label = legend)
    plt.title(title)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.legend()
    plt.show()


def bestfit(x, y):
    ''' This function takes two lists and finds the line of bestfit'''
    best = np.polyfit(x, y, 2, full = True)
    plt.plot(x, np.poly1d(np.polyfit(x, y, 2))(x))
    return best 
 
     
def poly(guess):
    '''This is a polynomial chi squared sum. The argument requires a list of
    three variables and x and y lists must be defined outside of the function
    in the porgram'''
    arx = np.asarray(x1)
    ary = np.asarray(y1)
    return sum(np.power(guess[0]*np.power(arx, 2) + guess[1]*arx + guess[2] - ary, 2))
  
  
def gauss(guess):
    '''This is a gaussian chi squared sum. The argument requires a list of
    three variables and x and y lists must be defined outside of the function
    in the porgram'''
    arx = np.asarray(x1)
    ary = np.asarray(y1)
    return sum(np.power(guess[0]*np.exp(-np.power((arx-guess[1]), 2)/(2*np.power(guess[2], 2))) + guess[3]*arx + guess[4] - ary, 2))
    
    
def optimize(f, guess):
    '''Takes a function and potential parameters and outputs the minimized 
    values for the guess'''
    fit = minimize(f, guess, method= 'Nelder-Mead', bounds = ((0, None), (0, None), (0, None), (None, 0), (0, None), (0, None),\
        (0, None), (0, None), (0, None), (None, None), (None, None)))
    return fit
   
     
def linefitpoly(opt, x, title, xname, yname, legend):
    ''' This plots the line of best fit from the optimize function for a 
    ploynomial'''
    ans = list(opt.x)
    ct = 0
    y = []
    for i in x:
        y.append(ans[0]*np.power(x[ct], 2) + ans[1]*x[ct] + ans[2])
        ct += 1
    plt.plot(x, y, label = legend)
    plt.title(title)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.legend()
    plt.show()


def linefitgauss(opt, x, title, xname, yname, legend):
    ''' This plots the line of best fit from the optimize function for a 
    ploynomial'''
    ans = list(opt.x)
    i = 0
    y = []
    for i in x:
        y.append(ans[0]*np.exp(-np.power((i-ans[1]), 2)/(2*np.power(ans[2], 2)))+ ans[3]*i + ans[4])
    plt.plot(x, y)
    plt.plot(x, y, label = legend)
    plt.title(title)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.legend()
    plt.show()

    
def linefitgaussRn(opt, x, title, xname, yname, legend):
    ''' This plots the line of best fit from the optimize function for a 
    ploynomial'''
    ans = list(opt.x)
    i = 0
    y = []
    for i in x:
        y.append(ans[0]*np.exp(-np.power((i-ans[1]), 2)/(2*np.power(ans[2], 2)))+\
            ans[3]*np.exp(-np.power((i-ans[4]), 2)/(2*np.power(ans[5], 2))) +\
            ans[6]*np.exp(-np.power((i-ans[7]), 2)/(2*np.power(ans[8], 2)))+ ans[9]*i + ans[10])
    plt.plot(x, y)
    plt.plot(x, y, label = legend)
    plt.title(title)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.legend()
    plt.show()        
            
                
def gaussRn(guess):
    '''This is a gaussian chi squared sum. The argument requires a list of
    three variables and x and y lists must be defined outside of the function
    in the porgram'''
    arx = np.asarray(x1)
    ary = np.asarray(y1)
    return sum(np.power(guess[0]*np.exp(-np.power((arx-guess[1]), 2)/(2*np.power(guess[2], 2)))\
        + guess[3]*np.exp(-np.power((arx-guess[4]), 2)/(2*np.power(guess[5], 2))) + \
        guess[6]*np.exp(-np.power((arx-guess[7]), 2)/(2*np.power(guess[8], 2))) + arx*guess[9] + guess[10] - ary, 2))
                                                      
                                           

def resolution(opt):
    '''This finds the resolution of the fit using the width, standard deviation
    and the center, the mean'''
    values = list(opt.x)
    return values[2]/values[1]
    

def conversion(opt, y):
    '''Automated Line of Best Fit for gamma and electron sources'''
    y = []
    x = []
    rawx =[]
    for i in opt:
        rawx.append(i)
    for i in rawx:
        x.append(i[1])
    for i in y:
        y.append(i)
    plt.errorbar(x, y, xerr = (opt[0][0], opt[1][0], opt[2][0]))
    plt.scipy.stats.linregress(x, y)
    plt.show()




guessregress = [11, 50]
    
def line(x, i, j):
    ''' A linear function'''
    return i*x + j    


def chan_kev():
    '''By replacing the x, y, and err values the function plots the points with
    their error and plots the line of bestfit'''
    x = [60, 511, 662, 1170, 1274, 1330]
    y = [702.5, 5738.7, 7425.6, 11826.8, 14363.2, 13681.8]
    err = [129.9, 325.4, 368.3, 790.2, 398.9, 421]
    names = [' ', 'Na-22 First  ', 'Cs-137  ', 'Co-60 First  ', 'Na-22 Second  ', 'Co-60 Second  ']
    first = ['  AmBe-241']
    yfit = []
    linfit = curve_fit(line, x, y, guessregress, sigma = err)
    for i in range(1400):
        yfit.append(i*linfit[0][0] + linfit[0][1])
    plt.errorbar(x, y, yerr= err, linestyle = 'None', marker = 'o', label = 'Raw Data Points')
    plt.plot(range(1400), yfit, label = 'Line of Best Fit')
    plt.ylim(-100, 17000)
    plt.title('Channel to Kev Count for Four Radioactive Sources')
    plt.xlabel('Known Particle Energy (KeV)')
    plt.ylabel('Channels (ADC)')
    plt.legend(loc = 2)
    
    for i, txt in enumerate(names):
        plt.annotate(txt, (x[i],y[i]), ha = 'right')
        plt.show()
    for i, txt in enumerate(first):
        plt.annotate(txt, (x[i], y[i]), ha = 'left')
        plt.show()
    plt.show()    
    print linfit
    
    
def radium():
    '''x represents the known keV values for the Ra impurities and y represents 
    the measured values in channels. This function outputs the quenching factor 
    for each measurement'''
    known = [4800, 5500, 6000, 7700]
    measured = [14721.6, 17577.5, 20210.9, 28612.8]
    error1 = [988.1, 657.6, 882.8, 723.2]
    error2 = []
    names = ['Ra-226    ', 'Ra-222    ', 'Po-218   ', 'Po-214    ']
    coun = 0
    tick = 0
    quench = []
    yfit = []
    for i in measured:
        pred = i*.085
        quench.append(known[coun]/pred)
        coun += 1
    linfit = stats.linregress(known, quench)
    for i in range(8000):
        yfit.append(i*linfit[0] + linfit[1])
    for i in error1:
        exper = measured[tick]
        recor = known[tick]
        error2.append((i*recor)/(math.pow(exper, 2)))
        tick += 1
    plt.plot(range(8000), yfit, label = 'Line of Best Fit')
    plt.xlim(4000, 8000)
    plt.errorbar(known, quench, yerr = error2, marker = 'o', linestyle = 'None', label = 'Quenching Factor')
    plt.title('Quenching Factor at Various Energies for Ra 226 in BaF2')
    plt.xlabel('Energy in keV')
    plt.ylabel('Quenching Factor (Birks Constant)')
    plt.legend(loc = 1)
    for i, txt in enumerate(names):
        plt.annotate(txt, (known[i],quench[i]), ha = 'right')
        plt.show()
    plt.show()
    return quench
    
    

  
a = -.000001
b = .2
c = -1600

para = [a, b, c]

hyp = [500, 14500, 1000, -.1, -.0001]

threepeaks = [500, 11000, 600, 140, 14000, 1000, 100, 15800, 1100, 0, 0]

x1 = energy(alldata('RaSB2170.txt')[0], alldata('RaSB2170.txt')[1], 20000, 9000)[0]
y1 = energy(alldata('RaSB2170.txt')[0], alldata('RaSB2170.txt')[1], 20000, 9000)[1]  
        
rawdata(x1, y1, 'Ra 226 4800, 5500, and 6000 keV Peaks at 2170 Volts SB', 'Energy in Channels', 'Counts', 'Collected Data (Observed)')
fitted = optimize(gaussRn, threepeaks)
linefitgaussRn(fitted, x1, 'Ra 226 4800, 5500, and 6000 keV Peaks at 2170 Volts SB', 'Energy in Channels', 'Counts', 'Gaussian Fit to Data')
print resolution(fitted)
print fitted.x



    
    


    