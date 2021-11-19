# Mood-and-audio-analyser

**What it does**

This is a gui aplication which I designed for the analysis of audio files. It uses in vocal audio files of the wav format (of which you can select yourself). It features mood detection, statistic gathering and visualisation plus some other features.

**Audio selection**

To choose your audio file, click on the "select audio" button, this will bring up your file system where you can navigate to the file you want to analyse, the path to your file will be shown on the bottom left of the screen.

**Mood analysis**

One of the more interesting things the software can do is run a mood detection script that based on a few variables (age, gender, pitch and in the future amplitude) which will return a guess of the mood you were in when you spoke. Remember to fill in the gender and age fields before running this. Note that this feature is not always 100% accurate as audio files have imperfections that can mess up the analysis (especially frequencu detection). **Also note that the longer the audio file, the less accurate this feature will be as its stats are based on averages...**

**Audio statistics analysis**

The software will allow you to visualise youe audio files in matplotlib using FFT for frequency analysis. You can also view average frequencys and amplitudes with th click of a button.

**Software**

This software was made using python, the frameworks and librarys it features are as follows: 
-Tkinter
-Playsound
-Numpy
-Aubio
-Scipy

**To try out**

Clone this repository and run the file titled gui.py. Make sure you have the correct modules installed...



