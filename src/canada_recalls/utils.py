import pandas as pd
import numpy as np

BASE = 'http://data.tc.gc.ca/v1.3/api/eng/vehicle-recall-database/'


def mutlipleParams(values):

    if not values:
        return None
    
    
    if type(values) == str:
        return values

    s = values.pop(0)

    if not values:
        return s
    
    for value in values:
        s += "|" + value

    return s

def param_concat(params):
    s = ''
    for k,v in params.items():
        if v:    
            s += k + '/' + str(v) + '/'

    return s
