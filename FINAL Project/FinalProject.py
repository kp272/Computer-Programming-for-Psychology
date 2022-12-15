

#=====================
#IMPORT MODULES
#=====================
from psychopy import gui, core, event, visual, monitors
import numpy as np
import csv
import json as json
import pandas as pd
import os
from datetime import datetime 
import random

#=====================
#PATH SETTINGS
#=====================
directory = os.getcwd()                         # defines the main directory (where the PsychoPy code file is saved) where experiment info is stored       
path = os.path.join(directory, 'dataFiles') 

#=====================
#COLLECT PARTICIPANT INFO
#=====================
expInfo = {'subject_nr': (), 'age': (), 'handedness':('right','left','ambi'), 'gender':(), 'session': 1}
my_dlg = gui.DlgFromDict(dictionary = expInfo, title = "subject info", fixed = ['session'], order = ['session', 'subject_nr', 'age', 'gender', 'handedness'])
expInfo['date'] = datetime.now()
filename = (str(expInfo['subject_nr']) + '_output10.csv') 

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
nBlocks = 1
nTrials = 18
totalTrials = nTrials*nBlocks
trial_timer = core.Clock()

#=====================
#PREPARE CONDITION LISTS
#=====================
colour = ['green'] + ['red'] + ['blue'] + ['red'] + ['blue'] + ['green'] + ['red'] + ['green'] + ['blue'] + ['green'] + ['blue'] + ['red'] + ['red'] + ['green'] + ['blue'] + ['green'] + ['blue'] + ['red'] 
word = ['dog'] + ['cat'] + ['house'] + ['bottle'] + ['blanket'] + ['pan'] + ['red'] + ['green'] + ['blue'] + ['green'] + ['blue'] + ['red'] + ['green','blue','red','blue','red','green'] 
 
trials = (list(zip(word,colour))) * 3


#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
colours = [0]*totalTrials                   # creates a "colours" list, with zeros for each trial, that looks like this --> "[0, 0, 0, 0, 0, 0]
accuracies = [0]*totalTrials                # creates a "accuracies" list, with zeros for each trial, that looks like this --> "[0, 0, 0, 0, 0, 0]
responseTimes = [0]*totalTrials             # creates a "responseTimes" list, with zeros for each trial, that looks like this --> "[0, 0, 0, 0, 0, 0]
trialNumbers = [0]*totalTrials              # creates a "trialNumbers" list, with zeros for each trial, that looks like this --> "[0, 0, 0, 0, 0, 0]
blockNumbers = [0]*totalTrials 
words = [0]*totalTrials
keys = [0]*totalTrials
condition = 'neutral', 'neutral','neutral','neutral','neutral','neutral', 'congruent', 'congruent','congruent','congruent','congruent','congruent','incongruent', 'incongruent','incongruent','incongruent','incongruent','incongruent'

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
mon = monitors.Monitor('myMonitor', width=35.89, distance=60)       #define the monitor parameters
mon.setSizePix([1440, 900])
win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1])  #define a window
fixation = visual.TextStim(win, text = '+')
stim = visual.TextStim(win)

#=====================
#START EXPERIMENT
#=====================

#=====================
#BLOCK SEQUENCE
#=====================
for block in range(nBlocks):
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        fixation.draw()
        win.flip()
        core.wait(.250)
        #=====================
        #START TRIAL
        #===================== 
        overallTrial = block*nTrials+trial 
        trialNumbers[overallTrial] = trial+1
        colours[overallTrial] = trials[overallTrial][1]
        words[overallTrial] = trials[overallTrial][0] 
        
        stim.text = trials[overallTrial][0]
        stim.color = trials[overallTrial][1]
        stim.draw()
        win.flip()
        
        trial_timer.reset()
          
        keys = event.waitKeys(keyList=['r', 'g', 'b'])
        
        if keys:
            responseTimes[overallTrial] = trial_timer.getTime() 
            if trials[overallTrial][1] == 'red':
                if keys[0] == 'r':
                    accuracies[overallTrial] = 'Correct'
                else:
                    accuracies[overallTrial] = 'Incorrect'
            if trials[overallTrial][1] == 'green':
                if keys[0] == 'g':
                    accuracies[overallTrial] = 'Correct'
                else: 
                    accuracies[overallTrial] = 'Incorrect'
            if trials[overallTrial][1] == 'blue':
                if keys[0] == 'b':
                    accuracies[overallTrial] = 'Correct'
                else: 
                    accuracies[overallTrial] = 'Incorrect'
            
        print('Trial:', trial+1, ', Word:', trials[overallTrial][0], ', Ink Colour:', trials[overallTrial][1] , ', Accuracy:', accuracies[overallTrial], ', Subject response:', keys, ', RT:', responseTimes[overallTrial])

df = pd.DataFrame(data={
 "Trial Number": trialNumbers, 
 "Word": words,
 "Condition": condition,
 "Ink Colours": colours, 
 "Accuracy": accuracies, 
 "Response Time": responseTimes
})
df.to_csv(os.path.join(path, filename), sep=',', index=False)

#======================
# END OF EXPERIMENT
#======================  
win.close()

