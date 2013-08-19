__author__ = 'polera'
__email__ = 'james@uncryptic.com'
__since__ = '2011-10-17'

from random import choice


class Srambler(object):

    ALPHAS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMS = "0123456789"
    BOOLS = [True, False]
    NON_ALPHAS = [' ', ',', '.', '$', '-']

    TYPE_MAP = {float: [NUMS, float],
                str: [ALPHAS, str],
                bool: [BOOLS, bool],
                int: [NUMS, int]}

    @staticmethod
    def srambled(subject):
        if subject is None:
            return None

        (pick_list, converter) = Srambler.TYPE_MAP[type(subject)]
        if pick_list != Srambler.BOOLS:
            sramble = ""
            for character in str(subject):
                if character.isdigit():
                    sramble += choice(Srambler.NUMS)
                    continue
                if character not in Srambler.NON_ALPHAS:
                    sramble += choice(pick_list)
                else:
                    sramble += character
        else:
            sramble = choice(pick_list)
        return converter(sramble)

scramble = Srambler.srambled
