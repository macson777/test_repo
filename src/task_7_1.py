def inch_to_cm(n):
    inch = n * 2.54
    return inch

def cm_to_inch(n):
    cm = n / 2.54
    return cm

def miles_to_km(n):
    ml = n * 1.609
    return ml

def km_to_miles(n):
    km = n / 1.609
    return km

def pound_to_kilo(n):
    kg = n / 2.204
    return kg

def kilo_to_pound(n):
    pound = n * 2.204
    return pound

def unc_to_gram(n):
    g = n * 28.35
    return g

def gram_to_unc(n):
    unc = n / 28.35
    return(unc)

def gal_to_l(n):
    l = n * 4.54
    return l
def l_to_gal(n):
    gal = n / 4.54
    return gal

def pint_to_l(n):
    l = n * 0.568
    return l

def l_to_pint(n):
    pint = n / 0.568
    return pint


print(l_to_pint(5))