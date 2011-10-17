__author__ = 'polera'
__email__ = 'james@uncryptic.com'
__since__ = '2011-10-17'

from random import choice
from types import FloatType, StringType, IntType, BooleanType

class Srambler(object):

    ALPHAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    NUMS   = "0123456789"
    BOOLS  = [True,False]
    NON_ALPHAS = [' ',',','.','$','-']

    TYPE_MAP = {FloatType:[NUMS,float],
                     StringType:[ALPHAS,str],
                     BooleanType:[BOOLS,bool],
                     IntType:[NUMS,int]}

    def __init__(self, subject):
        self.subject = subject

    @property
    def srambled(self):
        if self.subject is None:
            return self.subject
        
        pick_list = self.TYPE_MAP[type(self.subject)][0]
        converter = self.TYPE_MAP[type(self.subject)][1]
        if pick_list != self.BOOLS:
            sramble  = ""
            for character in str(self.subject):
                if character.isdigit():
                    sramble += choice(self.NUMS)
                    continue
                if character not in self.NON_ALPHAS:
                    sramble += choice(pick_list)
                else:
                    sramble += character
        else:
            sramble = choice(pick_list)
        return converter(sramble)
        


