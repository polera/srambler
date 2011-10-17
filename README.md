Srambler
========

Srambler is a utility class to assist with tasks like sanitizing data for a developer DB or, for just
scrambling strings/ints/floats/bools.

Why is it called Srambler
-------------------------
"Srambler" is how my four year old said the word "scrambler" when he was around 2 years old.  Also, Web 2.0 and
 marketing firms have conditioned me to spell things incorrectly.

How do I use it?
----------------
Put srambler in your Python path then:

    >>> from srambler import Srambler
    >>> Srambler("Jimmy Page").srambled
    'YBNnm seua'
    >>> Srambler("867-5309").srambled
    '949-1209'
    >>> Srambler(True).srambled
    True
    >>> Srambler(True).srambled
    False
    >>> Srambler("$33.49").srambled
    '$86.13'
    >>> Srambler(1620).srambled
    2280

