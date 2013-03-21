#!/usr/bin/env python
"""
wololo.py - 14 14 14 14 14 14 14 14
"""
import pickle

wololotable = {'1' : 'Yes.', \
               '2' : 'No.', \
               '3' : 'Food, please.', \
               '4' : 'Wood, please.', \
               '5' : 'Gold, please.', \
               '6' : 'Stone, please.', \
               '7' : 'Ahhhhhh!', \
               '8' : 'All hail King of the losers!', \
               '9' : 'Ooooohhhh.', \
               '10' : 'I\'ll beat you back to Age of Empires.', \
               '11' : '*Laugh*', \
               '12' : 'Ack! Bein\' rushed!', \
               '13' : 'Sure, blame it on your isp.', \
               '14' : 'Start the game already!', \
               '15' : 'Don\'t point that thing at me.', \
               '16' : 'Enemy sighted.', \
               '17' : 'It is good to be the king.', \
               '18' : 'Monk! I need a monk!', \
               '19' : 'Long time no seige.', \
               '20' : 'My granny can scrap better than that.', \
               '21' : 'Nice town, I\'ll take it.', \
               '22' : 'Quit touching me.', \
               '23' : 'Raiding party!', \
               '24' : 'Dadgum.', \
               '25' : 'Smite me!', \
               '26' : 'The wonder, the wonder, noooooo.', \
               '27' : 'You played 2 hours to die like this?!', \
               '28' : 'You should see the other guy.', \
               '29' : 'Roggan.', \
               '30' : 'Wololo.'}

def wololo(jenni, input):
    wololo = input.group(2)
    if wololo is None:
        return
    roggan = wololotable.get(wololo)
    if roggan is not None:
        jenni.say(roggan)
wololo.rule = r'(?i)(^)([1-9][0-9]?)[ \t]*$'

if __name__ == '__main__': 
   print __doc__.strip()
