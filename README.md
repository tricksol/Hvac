# Trick_Hvac />

This project is to use a Raspberry Pi to control my Heat and AC. <br/>

Main System uses 24v AC

Red = 24VAC
Green = FAN - ON / AUTO
YELLOW = HEAT - ON / OFF
WHITE = AC - ON / OFF

HVAC is single unit with 2 zones. 2 x 24VDC 3 wire dampers in the normally closed position.

System already has durazone controler so we will will only need to apply power to the thermostat wires to activate the system. When system is trigger by thermostat wire the dapmer for that zone automacally opens.

zone1 = downstairs
zone2 = upstairs

IF AC or heat is on an other is selected or called by profile disable system
for 5min. This is the short time to allow compressor pressure to return back to normal. Since my system is not an heat pump it doesn't matter but for good measure were going to do it do allow for duct cooling to happen.

Check temp 
Store number as raw from the sensor so can be converterd to C or F

Reach set temp goal +/- 1 turn off system for 15min. Start wait timer. 

Heat should be +1 and AC should be -1





