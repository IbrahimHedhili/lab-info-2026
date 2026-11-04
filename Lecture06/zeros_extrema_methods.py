def bisezione (
    g,              # funzione di cui trovare lo zero
    xMin,           # minimo dell'intervallo          
    xMax,           # massimo dell'intervallo         
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola zeri
    con il metodo della bisezione
    '''
    xAve = xMin 
    while ((xMax - xMin) > prec) :
        xAve = 0.5 * (xMax + xMin) 
        if (g (xAve) * g (xMin) > 0.): xMin = xAve 
        else                         : xMax = xAve 
        if(g(xAve) == 0): return xAve
    return xAve 

def bisezione_ricorsiva (
    g,              # funzione di cui trovare lo zero  
    xMin,           # minimo dell'intervallo            
    xMax,           # massimo dell'intervallo          
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola zeri
    con il metodo della bisezione ricorsivo
    '''
    xAve = 0.5 * (xMax + xMin)
    if(g(xAve) == 0): return xAve
    if ((xMax - xMin) < prec): return xAve ;
    if (g (xAve) * g (xMin) > 0.): return bisezione_ricorsiva (g, xAve, xMax, prec) ;
    else                         : return bisezione_ricorsiva (g, xMin, xAve, prec) ;

def golden_ratio_search_method (
    g,              # funzione di cui trovare l'estremo
    xMin,           # minimo dell'intervallo          
    xMax,           # massimo dell'intervallo         
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola l'estremo
    con il metodo della bisezione
    '''
    
    while(xMax - xMin > prec):
        x_r = 0.618 * (xMax - xMin) + xMin
        x_1_r = xMin + (1 - 0.618) *  (xMax - xMin)
        if(g(x_r) < g(x_1_r)):
            xMin = x_1_r
        else:
            xMax = x_r
    
    return (xMax + xMin)* 0.5

def golden_ratio_search_method_recursive (
    g,              # funzione di cui trovare l'estremo
    xMin,           # minimo dell'intervallo          
    xMax,           # massimo dell'intervallo         
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola l'estremo
    con il metodo della bisezione
    '''
    if xMax - xMin > prec : return (xMax + xMin) * 0.5

    x_r = 0.618 * (xMax - xMin) + xMin
    x_1_r = xMin + (1 - 0.618) *  (xMax - xMin)

    if(g(x_r) < g(x_1_r)):
        return golden_ratio_search_method_recursive(g,x_1_r, xMax)
    else:
        return golden_ratio_search_method_recursive(g, xMin, x_r)

import math

def golden_ratio_search_method_2 (
    g,              # funzione di cui trovare l'estremo
    xMin,           # minimo dell'intervallo          
    xMax,           # massimo dell'intervallo         
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola l'estremo
    con il metodo della bisezione
    '''
    R = (math.sqrt(5) - 1) * 0.5
    x_r = R * (xMax - xMin) + xMin
    x_1_r = xMin + (xMax - x_r)
    while(xMax - xMin > prec):

        if(g(x_r) < g(x_1_r)):
            xMin = x_1_r
            x_1_r = x_r
            x_r = xMax - (x_1_r - xMin)
        else:
            xMax = x_r
            x_r = x_1_r
            x_1_r = xMin + (xMax - x_r)
    
    return (xMax + xMin)* 0.5


def golden_ratio_search_method_maximum_recursive (
    g,              # funzione di cui trovare l'estremo
    xMin,           # minimo dell'intervallo          
    xMax,           # massimo dell'intervallo         
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola l'estremo
    con il metodo della bisezione
    '''
    if xMax - xMin > prec : return (xMax + xMin) * 0.5

    x_r = 0.618 * (xMax - xMin) + xMin
    x_1_r = xMin + (1 - 0.618) *  (xMax - xMin)

    if(g(x_r) > g(x_1_r)):
        return golden_ratio_search_method_recursive(g,x_1_r, xMax)
    else:
        return golden_ratio_search_method_recursive(g, xMin, x_r)
    
