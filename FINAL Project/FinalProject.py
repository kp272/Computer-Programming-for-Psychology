
# There should be 3 blocks of 12 trials each. 
# Each trial should have a single colour word in a single colour ink (pixels). 
# Use the colours 'red', 'green', and 'blue'. 
# Each block should have 
    # 6 "congruent" trials where the colour word and colour match (2 of each of the three colours), 
    # 6 "incongruent" trials where they don't match (each combination of color word and ink colour that don't match = 3 colours * 2 incongruent names each = 6.
# pressing letters ('r', 'g', or 'b') to indicate the ink colour 
# record 
    # trial             (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    # block             (1, 2, 3)
    # word              ('red', 'green', 'blue')
    # ink colour        (red, green, blue)
    # response          ('r', 'g', 'b')
    # accuracy          (Correct, Incorrect)
    # reaction time     (seconds)
# You will save these into a csv output file formated as in the example in Q6 & Q7.
# Words should appear 
    # following a fixation shown for 250 ms on each trial, 
    # and should remain on the screen until the response is collected

# each block looks like this and we randmize this:
# congruent (6 trials)
    # red in red
    # red in red
    # green in green 
    # green in green
    # blue in blue
    # blue in blue

# in congruent (6 trials)
    # red in green
    # red in blue
    # green in red 
    # green in blue
    # blue in red
    # blue in green

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
filename = (str(expInfo['subject_nr']) + '_output.csv') 

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
nBlocks = 2
nTrials = 18
totalTrials = nTrials*nBlocks
trial_timer = core.Clock()

#=====================
#PREPARE CONDITION LISTS
#=====================
colour = ['green'] + ['red'] + ['blue'] + ['red'] + ['blue'] + ['green'] + ['red'] + ['green'] + ['blue'] + ['green'] + ['blue'] + ['red'] + ['red'] + ['green'] + ['blue'] + ['green'] + ['blue'] + ['red'] 
word = ['dog'] + ['cat'] + ['house'] + ['bottle'] + ['blanket'] + ['pan'] + ['red'] + ['green'] + ['blue'] + ['green'] + ['blue'] + ['red'] + ['green','blue','red','blue','red','green'] 
condition = ['neutral'] * 6 + ['congruent'] * 6 + ['incongruent'] * 6

trials = (list(zip(word,colour,condition))) * 2
print(trials)
np.random.shuffle(trials)


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
conditions = [0]*totalTrials

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
    np.random.shuffle(trials)
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
        blockNumbers[overallTrial] = block+1
        colours[overallTrial] = trials[overallTrial][1]
        words[overallTrial] = trials[overallTrial][0] 
        conditions[overallTrial] = trials[overallTrial][2]
        
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
            
        print('Block:', block+1, ',Trial:', trial+1, ',Condition:', trials[overallTrial][2], ', Word:', trials[overallTrial][0], ', Ink Colour:', trials[overallTrial][1] , ', Accuracy:', accuracies[overallTrial], ', Subject response:', keys, ', RT:', responseTimes[overallTrial])

df = pd.DataFrame(data={
 "Block Number": blockNumbers,
 "Trial Number": trialNumbers, 
 "Condition": conditions,
 "Word": words,
 "Ink Colours": colours,
 "Accuracy": accuracies, 
 "Response Time": responseTimes
})
df.to_csv(os.path.join(path, filename), sep=',', index=False)

#======================
# END OF EXPERIMENT
#======================  
win.close()

