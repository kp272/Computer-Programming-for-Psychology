### Experiment structure exercises

#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np
#-import psychopy functions
#-import file save functions
#-(import other functions as necessary: os...)

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
#-define the directory where you will save your data
#-if you will be presenting images, define the image directory
#-check that these directories exist

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, 
    #handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 10
nBlocks = 2
#-stimulus names (and stimulus extensions, if images) *
objects = ['face'] * 10
pics = ['face01.jpg','face02.jpg','face03.jpg','face04.jpg','face05.jpg','face06.jpg','face07.jpg','face08.jpg','face09.jpg','face10.jpg']
#-stimulus properties like size, orientation, location, duration *
stimSize = [200,200]
stimDur = 1
#-start message text *
startMessage = "Welcome to the experiment. Press any key to begin"

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
#-create counterbalanced list of all conditions *
catimgs = list(zip(objects, pics))
    #print(catimgs)

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is 
    #correct") *
corrResp = [];
corrResp = np.zeros(20);

#-create an empty list for participant responses (e.g., "on this trial, response was a 
    #X") *
partResp = [];
partResp = np.zeros(20);

#-create an empty list for response accuracy collection (e.g., "was participant 
    #correct?") *
respAccu = [];
respAccu = np.zeros(20);

#-create an empty list for response time collection *
respTime = [];
respTime = np.zeros(20);

#-create an empty list for recording the order of stimulus identities *
stimOrd_iden = [];
stimOrd_iden = np.zeros(20);

#-create an empty list for recording the order of stimulus properties *
stimOrd_prop = [];
stimOrd_prop = np.zeros(20);

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for thisBlock in range(nBlocks):
    #-present block start message
    #-randomize order of trials here *
    np.random.shuffle(catimgs)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for thisTrial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment
