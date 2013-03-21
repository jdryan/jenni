#!/usr/bin/env python
"""
shazbot.py - Tribes Taunts
VGS VGS VGS
john@shiftregister.net
"""
import pickle

vgstable = { 'VGCA' : 'Awesome!', \
             'VGCG' : 'Good game', \
             'VGCN' : 'Nice move!', \
             'VGCS' : 'Great shot!', \
             'VGCY' : 'You Rock!', \
             'VGRA' : 'Any time.', \
             'VGRD' : 'I don\'t know.', \
             'VGRT' : 'Thanks.', \
             'VGRW' : 'Wait.', \
             'VGTA' : 'Aww, that\'s too bad!', \
             'VGTB' : 'Is that the best you can do?', \
             'VGTG' : 'I am the greatest!', \
             'VGTT' : 'THAT was graceful!', \
             'VGTW' : 'When will you learn?', \
             'VGY' : 'Yes.', \
             'VGN' : 'No.', \
             'VGH' : 'Hi.', \
             'VGB' : 'Bye.', \
             'VGO' : 'Oops.', \
             'VGQ' : 'Quiet!', \
             'VGS' : 'Shazbot!', \
             'VGW' : 'Woohoo!', \
             'VAA' : 'Attack!', \
             'VAB' : 'Attack the enemy base!', \
             'VAC' : 'Chase the enemy flag carrier!', \
             'VAD' : 'Disrupt the enemy defense!', \
             'VAF' : 'Get the enemy flag!', \
             'VAG' : 'Destroy the enemy generator!', \
             'VAR' : 'Reinforce the offense!', \
             'VAS' : 'Destroy enemy sensors!', \
             'VAT' : 'Destroy enemy turrets!', \
             'VAV' : 'Destroy the enemy vehicle!', \
             'VAW' : 'Wait for my signal before attacking!', \
             'VDB' : 'Defend our base!', \
             'VDC' : 'Defend the flag carrier!', \
             'VDE' : 'Defend the entrances!', \
             'VDF' : 'Defend our flag!', \
             'VDG' : 'Defend our generator!', \
             'VDM' : 'Cover me!', \
             'VDR' : 'Reinforce our defense!', \
             'VDS' : 'Defend our sensors!', \
             'VDT' : 'Defend our turrets!', \
             'VDV' : 'Defend our vehicle!', \
             'VRG' : 'Repair our generator!', \
             'VRS' : 'Repair our sensors!', \
             'VRT' : 'Repair our turrets!', \
             'VRV' : 'Repair the vehicle!', \
             'VBC' : 'Our base is clear.', \
             'VBE' : 'The enemy is in our base.', \
             'VBR' : 'Retake our base!', \
             'VBS' : 'Secure our base!', \
             'VCA' : 'Acknowledged.', \
             'VCC' : 'Completed.', \
             'VCD' : 'Declined.', \
             'VCW' : 'What\'s my assignment?', \
             'VED' : 'The enemy is in disarray.', \
             'VEG' : 'The enemy generator is destroyed.', \
             'VES' : 'The enemy sensors are destroyed.', \
             'VET' : 'The enemy turrets are destroyed.', \
             'VEV' : 'The enemy vehicle is destroyed.', \
             'VFD' : 'Defend our flag!', \
             'VFF' : 'I have the flag!', \
             'VFG' : 'Give me the flag!', \
             'VFR' : 'Retrieve our flag!', \
             'VFS' : 'Our flag is secure.', \
             'VFT' : 'Take the flag from me!', \
             'VNC' : 'Need covering fire. ', \
             'VND' : 'I need a driver.', \
             'VNE' : 'I need an escort.', \
             'VNH' : 'Hold that vehicle! I\'m coming!', \
             'VNR' : 'I need a ride!', \
             'VNS' : 'I need support!', \
             'VNV' : 'Vehicle ready. Need a ride?', \
             'VNW' : 'Where to?', \
             'VSAA' : 'I will attack.', \
             'VSAB' : 'I will attack the enemy base.', \
             'VSAF' : 'I\'ll go for the enemy flag.', \
             'VSAG' : 'I\'ll attack the enemy generator.', \
             'VSAS' : 'I\'ll attack the enemy sensors.', \
             'VSAT' : 'I\'ll attack the enemy turrets.', \
             'VSAV' : 'I\'ll attack the enemy vehicle.', \
             'VSDB' : 'I will defend our base.', \
             'VSDD' : 'I will defend.', \
             'VSDF' : 'I will defend our flag.', \
             'VSDG' : 'I\'ll defend our generator.', \
             'VSDS' : 'I\'ll defend our sensors.', \
             'VSDT' : 'I\'ll defend our turrets.', \
             'VSDV' : 'I\'ll defend our vehicle.', \
             'VSRV' : 'I\'ll repair the vehicle.', \
             'VSRG' : 'I\'ll repair our generator.', \
             'VSRS' : 'I\'ll repair our sensors.', \
             'VSRT' : 'I\'ll repair our turrets.', \
             'VSRV' : 'I\'ll repair the vehicle.', \
             'VSTC' : 'I\'ll cover you.', \
             'VSTD' : 'I\'ll set up defenses.', \
             'VSTF' : 'I\'ll deploy forcefields.', \
             'VSTO' : 'I\'m on it.', \
             'VSTS' : 'I\'m deploying sensors.', \
             'VSTT' : 'I\'m deploying turrets.', \
             'VSTV' : 'I\'ll get a vehicle ready.', \
             'VTA' : 'Target acquired.', \
             'VTB' : 'Target the enemy base! I\'m in position.', \
             'VTD' : 'Target destroyed.', \
             'VTF' : 'Target the enemy flag! I\'m in position.', \
             'VTM' : 'Fire on my target!', \
             'VTN' : 'I need a target painted!', \
             'VTS' : 'Target the sensors! I\'m in position.', \
             'VTT' : 'Target the turret! I\'m in position.', \
             'VTV' : 'Target the vehicle! I\'m in position.', \
             'VTW' : 'Wait! I\'ll be in range soon.', \
             'VWE' : 'Incoming hostiles!', \
             'VWV' : 'Incoming enemy vehicle!', \
             'VVY' : 'Yes.', \
             'VVN' : 'No.', \
             'VVA' : 'Anytime.', \
             'VVB' : 'Is our base secure?', \
             'VVC' : 'Cease fire!', \
             'VVD' : 'I don\'t know.', \
             'VVH' : 'Help!', \
             'VVM' : 'Move!', \
             'VVS' : 'Sorry.', \
             'VVT' : 'Thanks.', \
             'VVW' : 'Wait.', \
             'VGD' : 'Dammit!', \
             'VGE' : 'Duh!', \
             'VGX' : 'You idiot!', \
             'VGC' : 'Ah, crap!' }

def vgs(jenni, input):
    shaz = input.group(2)
    if shaz is None:
        return
    woohoo = vgstable.get(shaz.upper())
    if woohoo is None:
        uservgstable = openuservgs()
        woohoo = uservgstable.get(shaz.upper())
    if woohoo is not None:
        jenni.say(woohoo)
vgs.rule = r'(?i)(^)(v.{2,3})[ \t]*$'
vgs.priority = 'medium'
vgs.example = 'vgs'

def openuservgs():
    # read python dict back from the file
    try:
        pkl_file = open('vgsusertable.pkl', 'rb')
    except IOError:
        return {}
    vgsusertable = pickle.load(pkl_file)
    pkl_file.close()
    return vgsusertable

def saveuservgs(table):
    # write python dict to a file
    output = open('vgsusertable.pkl', 'wb')
    pickle.dump(table, output)
    output.close()

def remvgs(jenni, input):
    vgsusertable = openuservgs()
    shaz = input.group(2)
    if shaz is not None and shaz.upper() in vgsusertable:
        jenni.say('Removing...')
        del vgsusertable[shaz.upper()]
        saveuservgs(vgsusertable)
    else:
        jenni.say('Aww, that\'s too bad!')
remvgs.rule = r'(?i)(^remvgs: )(v.{2,3})[ \t]*$'
remvgs.priority = 'low'
remvgs.example = 'remvgs: vgbr'

def addvgs(jenni, input):
    jenni.say('Adding...')
    vgsusertable = openuservgs()
    shaz = input.group(2)
    if shaz is None or input.group(4) is None:
        return
    woohoo = vgstable.get(shaz.upper())
    if woohoo is None:
        woohoo = vgsusertable.get(shaz.upper())
    if woohoo is not None:
        jenni.say('I already know %s, it\'s %s' % (shaz, woohoo))
        return
    woohoo = input.group(4)
    vgsusertable[str(shaz.upper())]=str(woohoo)
    saveuservgs(vgsusertable)
addvgs.rule = r'(?i)(^addvgs: )(v.{2,3})(=")(.*)(")[ \t]*$'
addvgs.priority = 'low'
addvgs.example = 'addvgs: vgbr="It\'s beer thirty!"'


if __name__ == '__main__': 
   print __doc__.strip()
