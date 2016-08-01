# Ariel Hasse SURF 2016, Barium Floride Crystal Manufacturer Data Analysis

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize 
from scipy import stats
from scipy.optimize import curve_fit
import scipy.integrate as integrate
from scipy.interpolate import interp1d
            


def seg_lists(split):
    '''This program splits the global lists at a specified y value. It returns a tuple of
    four lists; x and y value for the first and second half of the split in data, respectively'''
    alldatax = wl1
    alldatay = intensity
    twox = []
    twoy = []
    onex = []
    oney = []
    for i in alldatay:
        if i == split:
            onex = alldatax
            oney = alldatay
            break
        else:
            twox.append(alldatax[i])
            twoy.append(alldatay[i])
            del alldatax[i]
            del alldatay[i]
    return (onex, oney, twox, twoy)
    
    


def specs():
    plt.plot(wl1, intensity, label = 'Intensity of Light')
    plt.title('Emission Spectrum for BaF2')
    plt.xlabel('Wavelength in Nanometers')
    plt.ylabel('Relative Light Intensity')
    plt.legend(loc = 2)
    plt.show()
    

def gauss4(guess):
    '''This is a gaussian chi squared sum. The argument requires a list of
    three variables and x and y lists must be defined outside of the function
    in the program'''
    arx = np.asarray(wl1)
    ary = np.asarray(intensity)
    return sum(np.power(guess[0]*np.exp(-np.power((arx-guess[1]), 2)/(2*np.power(guess[2], 2)))\
        + guess[3]*np.exp(-np.power((arx-guess[4]), 2)/(2*np.power(guess[5], 2))) + \
        guess[6]*np.exp(-np.power((arx-guess[7]), 2)/(2*np.power(guess[8], 2))) + \
        guess[9]*np.exp(-np.power((arx-guess[10]), 2)/(2*np.power(guess[11], 2))) - ary, 2))
        

def optimize(f, guess):
    '''Takes a function and potential parameters and outputs the minimized 
    values for the guess'''
    constr = [(0, None), (0, None), (0, None), (0, None), (0, None), (0, None),(0, None),\
                (0, None), (0, None), (0, None), (0, None), (0, None)]
    fit = minimize(f, guess, method= 'Nelder-Mead', bounds = constr)
    return fit
 
       
def linefitgauss4(opt, x, title, xname, yname, legend):
    ''' This plots the line of best fit from the optimize function for a 
    ploynomial'''
    ans = list(opt.x)
    i = 0
    y = []
    for i in x:
        y.append(ans[0]*np.exp(-np.power((i-ans[1]), 2)/(2*np.power(ans[2], 2)))+\
            ans[3]*np.exp(-np.power((i-ans[4]), 2)/(2*np.power(ans[5], 2))) +\
            ans[6]*np.exp(-np.power((i-ans[7]), 2)/(2*np.power(ans[8], 2))) +\
            ans[9]*np.exp(-np.power((i-ans[10]), 2)/(2*np.power(ans[11], 2))))
    plt.plot(x, y)
    plt.plot(x, y, label = legend)
    plt.title(title)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show() 
    
    
def slow_fast(opt):
    '''This function splits the four gaussian fit into the slow and fast components
    of the BaF2 crystal and then it plots the fits'''
    opti = opt.x
    x = list(range(150, 451))
    y_fast = []
    y_slow = []
    
    for i in range(150, 451):
        y_fast.append(opti[0]*np.exp(-np.power((i-opti[1]), 2)/(2*np.power(opti[2], 2)))\
        + opti[3]*np.exp(-np.power((i-opti[4]), 2)/(2*np.power(opti[5], 2))))
        
        y_slow.append(opti[6]*np.exp(-np.power((i-opti[7]), 2)/(2*np.power(opti[8], 2)))\
        + opti[9]*np.exp(-np.power((i-opti[10]), 2)/(2*np.power(opti[11], 2))))
    
    plt.plot(x, y_fast, label = 'Fast Component')
    plt.plot(x, y_slow, label = 'Slow Component')
    plt.title('Fits for the Slow and Fast Components (BaF2)')
    plt.xlabel('Wavelength in Nanometers')
    plt.ylabel('Relative Light Intensity')
    plt.legend(loc = 2)
    plt.show()
    


def comp_fast(x):
    '''Returns the function of the fast component with the fitted parameters'''
    return values[0]*np.exp(-np.power((x-values[1]), 2)/(2*np.power(values[2], 2)))\
        + values[3]*np.exp(-np.power((x-values[4]), 2)/(2*np.power(values[5], 2)))
        

def comp_slow(x):
    '''Returns the function of the fast component with the fitted parameters'''
    return values[6]*np.exp(-np.power((x - values[7]), 2)/(2*np.power(values[8], 2)))\
        + values[9]*np.exp(-np.power((x - values[10]), 2)/(2*np.power(values[11], 2)))   
    
        
    
def comp_perc(func1, func2):
    '''This function outputs the percentage of the curve that is the fast and slow
    componetns, respectively. It takes in a function for both the slow and fast fits'''
    fast = integrate.quad(func1, 150, 450)
    slow = integrate.quad(func2, 150, 450)
    fast_perc = (fast[0])/(fast[0] + slow[0])
    slow_perc = (slow[0])/(fast[0] + slow[0])
    print (fast_perc, slow_perc)

    
def gauss2(para):
    arx = np.asarray(wl1)
    conv = [0.0, 0.0, 0.0, 0.0, 0.0028000000000000004, 0.0057749999999999998, 0.0147, 0.027956249999999998, 0.048875000000000002, 0.048221250000000007, 0.04752, 0.041300000000000003, 0.052739999999999995, 0.079475000000000004, 0.094049999999999995, 0.08212499999999999, 0.066937500000000011, 0.045675000000000007, 0.04165, 0.0410125, 0.041562499999999995, 0.053437499999999999, 0.078375, 0.097700000000000009, 0.12299, 0.14818999999999999, 0.1716, 0.19795000000000001, 0.22550000000000001, 0.25110000000000005, 0.27451000000000003, 0.28810249999999998, 0.28749999999999998, 0.27960000000000002, 0.2596, 0.242925, 0.22312499999999999, 0.20315, 0.1875, 0.16200000000000001, 0.14099999999999999, 0.12547499999999998, 0.1115625, 0.10072500000000001, 0.09144999999999999, 0.080437499999999995, 0.075399999999999995, 0.069299999999999987, 0.064687499999999995, 0.059587500000000002, 0.053200000000000004, 0.049950000000000001, 0.045375000000000006, 0.040312500000000008, 0.036750000000000005, 0.032343750000000004, 0.029325, 0.022275, 0.017999999999999999, 0.014025000000000001, 0.011375000000000001]
    ary = np.asarray(conv)    
    return sum(np.power(para[0]*np.exp(-np.power((arx-para[1]), 2)/(2*np.power(para[2], 2)))\
        + para[3]*np.exp(-np.power((arx-para[4]), 2)/(2*np.power(para[5], 2))) + \
        para[6]*np.exp(-np.power((arx-para[7]), 2)/(2*np.power(para[8], 2))) + \
        para[9]*np.exp(-np.power((arx-para[10]), 2)/(2*np.power(para[11], 2))) - ary, 2))
       
                     
             
    
def convolve():
    quan = []
    conv = []
    coun = 0
    splfit = interp1d(wl2, quan_eff_rel)
    for i in wl1:
        quan.append(splfit(i))
    for i in intensity:
        conv.append(i*quan[coun])
        coun += 1
    fit = optimize(gauss2, para)
    linefitgauss4(fit, wl1, 'Convolution Fit', 'Wavelength in Nanometers', 'Relative Intensity', 'Gaussian Fit')
    plt.plot(wl1, conv, label = 'Convolution')
    plt.legend(loc = 2)
    plt.show()



def convolve_func():
    wl3 = list(range(150, 501, .1))
    quan = []
    inten = []
    conv = []
    coun = 0
    splfit = interp1d(wl2, quan_eff_rel)
    for i in wl3:
        inten.append()
    for i in wl3:
        quan.append(splfit(i))
    for i in inten:
        conv.append(i*quan[coun])
        coun += 1
        
    
   
       

    
wl1 = list(range(150, 451, 5))
wl2 = list(range(150, 501, 10))
intensity = [0, 0, 0, 0, .02, .03, .06, .105, .17, .165, .16, .14, .18, .275, \
        .33, .3, .255, .18, .17, .17, .175, .225, .33, .4, .49, .58, .66, .74, .82, \
        .9, .97, 1.01, 1, .96, .88, .82, .75, .68, .625, .54, .47, .42, .375, .34, \
        .31, .275, .26, .24, .225, .21, .19, .18, .165, .15, .14, .125, .115, .09, .075, .06, .05]
quan_eff = [0, 5, 14, 24.5, 28.75, 29.7, 29.3, 28.5, 26.25, 24.5, 23.75, 23.75,\
            25.1, 26, 27.5, 28.3, 28.75, 29.5, 29.75, 30, 30, 29.75, 29.5, 29, 28.75, \
            28, 27.5, 26.25, 25.5, 24, 22.75, 21.25, 19.5, 18, 16.25, 14.5]
outof = 100
quan_eff_rel = [float(x) / outof for x in quan_eff]
                    
                            
    
para = [.04, 190, 10, .1, 221, 14.8, .3, 305, 42.27, .08, 390, 61]

guess = [.16, 192, 12.06, .301, 221, 14.8, .91, 305, 42.27, .221, 376, 61]

fitted = optimize(gauss4, guess)
#values = list(fitted.x)
values = [4.81878721e-02, 1.92595247e+02, 7.78265493e+00, 8.62458430e-02, 2.20879193e+02, 1.07785755e+01, 2.53039186e-01, 3.06118184e+02, 2.86227125e+01, 6.88847019e-02, 3.67604375e+02, 4.52877055e+01]



#linefitgauss4(fitted, wl1, 'Quantum Efficiency by Wavelength for BaF2', 'Wavelength in Nanometers',\
#                'Relative Light Intensity', 'Light Intensity Fit')
#slow_fast(fitted)
comp_perc(comp_fast, comp_slow)
#convolve()
#specs()          




