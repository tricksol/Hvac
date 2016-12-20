# Trick_Hvac 

This project is to use a Raspberry Pi to control my Heat and AC. <br/>

Main System uses 24v AC

Red = 24VAC <br />
Green = FAN - ON / AUTO <br/>
YELLOW = HEAT - ON / OFF <br/>
WHITE = AC - ON / OFF <br/>

HVAC is single unit with 2 zones. 2 x 24VDC 3 wire dampers in the normally closed position.

System already has durazone controller so we will will only need to apply power to the thermostat wires to activate the system. When system is trigger by thermostat wire the damper for that zone automatically opens.

zone1 = downstairs <br/>
zone2 = upstairs <br />

IF AC or heat is on an other is selected or called by profile disable system
for 5min. This is the short time to allow compressor pressure to return back to normal. Since my system is not an heat pump it doesn't matter but for good measure were going to do it do allow for duct cooling to happen.

Check temp 
Store number as raw from the sensor so can be converted to C or F

Heat should be +1 and AC should be -1 

Reach set temp goal +/- 1 turn off system for 15min. Start wait timer.





