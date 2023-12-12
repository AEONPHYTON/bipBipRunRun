# bipBipRunRun
This project allows the coach to manage an incremental velocity test (like Mader's test).

The test is developed in a 400-meter track and field in the first lane. Put a cone every X meters (when X is the distance in meters between two cones).

Set the run pace per 1k in minutes and second separate by a dot (.)

Set the distance X (when you put the cone) and press CALCOLA

In the GUI appears the velocity in km/h and the time to run the distance X at the current pace. If the athlete runs regularly, every time is near the cone there's a "beep".

To stop the sound tap the button ARRESTA.

In synthesis, it's a kind of metronome.

Re-set the run pace and repeat till the end of the test

There are two types of scripts:
 
for Python users:
bip_bip.py
dependencies: PYQT5 - PYGAME - SYS

for a web-dev users:
bip.html
bipScript.js
bipStyle.css

note: the file beep.mp3 didn't upload on GitHub, choose or download one file for the signal and use it (remember to change the name of the file or the name in the import on the scripts)

You can find the working script on this website

https://klausermanspitzwegendorfentag.com/bip.html

