__author__ = 'fucus'
from django.db import models

class BaseInitWithDic(object):
    def __init__(self,dic):
        for key in dic.keys():
            if hasattr(self,key):
                setattr(self,key,dic[key])



