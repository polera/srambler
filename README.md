Srambler
========

Srambler is a utility class to assist with tasks like sanitizing data for a developer DB or, for just
scrambling strings/ints/floats/bools.

Why is it called Srambler?
-------------------------
"Srambler" is how my four year old said the word "scrambler" when he was around 2 years old.  Also, Web 2.0 and
 marketing firms have conditioned me to spell things incorrectly.

How do I use it?
----------------
Put srambler in your Python path then:

    >>> from srambler import Srambler
    >>> Srambler.srambled("Jimmy Page")
    'YBNnm seua'
    >>> Srambler.srambled("867-5309")
    '949-1209'

I realize it may become tedious to type srambled over and over again.  So, you could also do it this way:

    >>> from srambler import scramble
    >>> scramble("$33.49")
    '$86.13'
    >>> scramble(1620)
    2280

Status
------
Srambler is the product of an ad-hoc job (needed to sanitize some data before handing a SQL dump off via email),
and is still very young.  Next up are unit tests and some enhanced functionality.

Feedback is welcome!