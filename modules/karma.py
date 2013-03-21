#!/usr/bin/env python
"""
karma.py - A clumsy, possibly functional karma system
john@shiftregister.net

More info:
 * Jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""
import re, pickle
import datetime, time
import operator
twoseconds=datetime.timedelta(seconds=2)

# dict of channel/last person to talk that didn't say +1
LAST_NICK = {}

def loadkarma():
    # read python dict back from the file
    try:
        pkl_file = open('karma.pkl', 'rb')
    except IOError:
        return {}
    karmatable = pickle.load(pkl_file)
    pkl_file.close()
    return karmatable

KARMA = loadkarma()

def savekarma():
    # write python dict to a file
    output = open('karma.pkl', 'wb')
    pickle.dump(KARMA, output)
    output.close()

def getkarma(name):
    return KARMA.get(name, 0)
  
def setkarma(name,value):
    KARMA[name] = KARMA.get(name, 0) + int(value)
    savekarma()
    
def notify(jenni, recipient, text):
    jenni.write(('NOTICE', recipient), text)

def plusplus(jenni, input):
    name = input.group(1).lstrip().rstrip()

    #print "name=%s, LAST_NICK=%s" % (name, LAST_NICK.get(input.sender, 'aaa'))

    if name == '' or not name or len(name) == 0:
        name = LAST_NICK.get(input.sender, 'ShazBot')

    #print "name=%s, LAST_NICK=%s" % (name, LAST_NICK.get(input.sender, 'aaa'))

    if name == input.nick:
        print "%s downvoting %s" % (input.nick, name)
        setkarma(name, -1)
    else:
        print "%s upvoting %s" % (input.nick, name)
        setkarma(name, 1)
    #notify(jenni,input.nick,"%s is now at %d karma." % (name,getkarma(name)))

plusplus.rule = r'\+1(.*)$'
plusplus.priority = 'low'

def minusminus(jenni, input):
    print "%s downvoting %s" % (input.nick, str(input))
    name = input.group(1).lstrip.rstrip()

    if name == '' or not name or len(name) == 0:
        name = LAST_NICK.get(input.sender, 'ShazBot')

    print "%s downvoting %s" % (input.nick, name)
    setkarma(name,-1)

    #notify(jenni,input.nick,"%s is now at %d karma." % (name,getkarma(name)))

#  else:
#    notify(jenni,input.nick,"Please wait until 5 minutes after %s." % datetime.datetime.fromtimestamp(float(status)))
minusminus.rule = r'-1 (.*)$'
minusminus.priority = 'low'

def askkarma(jenni, input):
    name=input.group(1).lstrip().rstrip() or input.nick
    jenni.say("%s is at %d karma." % (name,getkarma(name)))
askkarma.rule=r'\.karma(.*)'

def karmarank(jenni, input):
    sorted_karma = sorted(KARMA.iteritems(), key=operator.itemgetter(1))
    losers = sorted_karma[:3]
    winners = sorted_karma[-3:]
    msg1 = ''
    for x in winners:
        msg1="%s:%s   " % (x[0], x[1]) + msg1
    msg1 = "Winners: " + msg1
    msg2 = "Losers: "
    for x in losers:
        msg2+="%s:%s   " % (x[0], x[1])
    jenni.say(msg1)
    time.sleep(0.5)
    jenni.say(msg2)
karmarank.rule=r'\.rank$'

def lastnick(jenni, input):
    if not '+1' in input.group(0):
        LAST_NICK[input.sender] = input.nick

lastnick.rule = r'.*'
