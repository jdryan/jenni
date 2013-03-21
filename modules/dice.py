#!/usr/bin/env python
"""
dice.py - Dice rolling module
john@shiftregister.net

More info:
 * Jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""

import random
import os

def diceroll(jenni, input):
    dice = int(input.group(1))
    sides = int(input.group(2))
    results = [0]
    output = input.nick + ': ' + str(dice) + 'd' + str(sides) + ': '

    if (1 <= dice < 1001 and 1 < sides < 1001):
        results = [random.randrange(1,sides) for x in xrange(dice)]
        if (dice < 11):
            output += str(results) + "  "
        output += "Total: " + str(sum(results))

    else:
        output = "Nope."
    
    jenni.say(output)
diceroll.rule='\!([0-9]+)d([0-9]+)'
diceroll.priority='low'
diceroll.example='!2d20'

if __name__ == '__main__':
    print __doc__.strip()
