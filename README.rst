Card Magic
===========
:Objective: Create and shuffle a deck of cards 52 cards, 13 faces, 4 suits
:Author: Juan Carlos Ferrer

About
-------
This is the best deck of cards ever.

Installation
-------------
::
    git clone git://github.com/juancferrer/Card-Magic.git
    cd Card-Magic
    python setup.py install


Example
------------------
::
    LANG=en_US.UTF-8 python demo.py 
        [7 Hearts, 12 Diamonds, 10 Hearts, 7 Clubs, 6 Hearts, 10 Diamonds, 12 Clubs]
    LANG=es_ES python demo.py 
        [1 Tréboles, 12 Tréboles, 13 Corazones, 7 Diamantes, 5 Picas, 2 Diamantes, 13 Picas]

Testing
--------
The easiest way to run the tests is to install the package as described above 
and run **python -m unittest discover -v** in the root
of the distribution. Tests are located in the *test/* directory.

