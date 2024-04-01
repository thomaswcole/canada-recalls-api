
import requests
import pandas as pd
from .utils import *


class CanadaRecalls:

    """Simple API to interact with Canadian Automotive Recalls Database"""


    def __init__(self,format = 'json'):

        self.format = '?format=%s' %format

        self.params =  {
            'recall-number':None,
            'make-name':None,
            'manufacturer-name':None,
            'minimum-model-year':None,
            'maximum-model-year':None,
            'year-range':None,
            'model-name':None,
        }

        self.__session = requests.session()

    
    def list(self,recallNumber = None,makeName = None,manufacturerName = None,minModelYear = None,maxModelYear = None,yearRange = None,modelName = None):
        
        params = {
            'recall-number':recallNumber,
            'make-name':makeName,
            'manufacturer-name':manufacturerName,
            'minimum-model-year':minModelYear,
            'maximum-model-year':maxModelYear,
            'year-range':yearRange,
            'model-name':modelName,
        }
        
        return self.__session.get(BASE + 'recall?format=json',params = params).json()
    
    def recallSummary(self,recallNum = None):
        __url = BASE + 'recall-summary/recall-number/' + str(recallNum) + self.format

        return self.__session.get(__url)

    def query(self,recallNumber = None,makeName = None,
              manufacturerName = None,minModelYear = None,
              maxModelYear = None,yearRange = None,modelName = None,count = False):
        
        """Query by all parameters"""
        
        self.params = {
            'recall-number':mutlipleParams(recallNumber),
            'make-name':mutlipleParams(makeName),
            'manufacturer-name':mutlipleParams(manufacturerName),
            'minimum-model-year':mutlipleParams(minModelYear),
            'maximum-model-year':mutlipleParams(maxModelYear),
            'year-range':mutlipleParams(yearRange),
            'model-name':mutlipleParams(modelName),
        }
        
        __url = BASE + 'recall/' + param_concat(self.params) + self.format

        if count:
            __url = BASE + 'recall/' + param_concat(self.params) +  "count" + self.format
        
        return self.__session.get(__url).json()
    

    

