# PsychoPy keypress exercises

1. event.getKeys is prone to collect as many responses as you can make in a trial, but often times you only want to collect one response for a trial. Come up with a solution so that only a single response is recorded from event.getKeys (e.g., ignoring all responses after the first response). Hint: one solution is used somewhere else in level6.

```
#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions
import numpy as np

#-import psychopy functions
from psychopy import core, gui, visual, event, monitors

#-import file save functions
import json

#-(import other functions as necessary: os...)
import os
from datetime import datetime



#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
print(os.getcwd())
main_dir = os.getcwd()
print(main_dir)

#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')

#-check that these directories exist
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")

# if not os.path.isdir(data_dir):
    # raise Exception("Could not find the path!")


#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, 
    #handedness
print("All variables have been created! Now ready to show the dialog box!")
exp_info = {'subject_nr': 0, 'age': 0, 'handedness':('right','left','ambi'), 'gender':(), 'session': 1}
print(exp_info)
print("All variables have been created! Now ready to show the dialog box!")
my_dlg = gui.DlgFromDict(dictionary = exp_info, title = "subject info", fixed = ['session'], order = ['session', 'subject_nr', 'age', 'gender', 'handedness'])

#get date and time
date = datetime.now()
exp_info['date'] = str(date.hour) + '-' + str(date.day) + '-' + str(date.month) + '-' + str(date.year)
print(exp_info['date'])

#-create a unique filename for the data
filename =  str(exp_info['subject_nr']) + '-' + exp_info['date'] + '.csv'
main_dir = os.getcwd()
sub_dir = os.path.join(main_dir,'sub_info',filename)

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 2
nBlocks = 2

#-stimulus names (and stimulus extensions, if images) *
cats = ['faces'] * 10
imgs = ['im1.png', 'im2.png', 'im3.png', 'im4.png', 'im5.png', 'im6.png', 'im7.png', 'im8.png', 'im9.png', 'im10.png']

#-stimulus properties like size, orientation, location, duration *
stimSize = [200,200];
stimDur = 1;
stimOri = [10];
stimLoc = [50,150]

#-start message text (check "CREATION OF WINDOW AND STIMULI" for a repeat of this)
startMessage = "Welcome to the experiment. Press any key to begin"

#=====================
#PREPARE CONDITION LISTS
#=====================
# Automate the creation of the list of images ("pics"). Do not write them all out manually.
           # pics = ['face01.jpg','face02.jpg','face03.jpg','face04.jpg','face05.jpg','face06.jpg','face07.jpg','face08.jpg','face09.jpg','face10.jpg']
           # 'face' + str(number) + .'jpg'
n = 0
pics = []
while n < 10:
    n = n + 1
    pics.append('face' + f'{n:02}' + '.jpg') 
print(pics)

ims_in_dir = sorted(os.listdir(image_dir))
print(ims_in_dir)

#-check if files to be used during the experiment (e.g., images) exist
    # 1) One way to do this is to use the code:
            # if not pics == ims_in_dir:
            # raise Exception("The image lists do not match up!")
    # 2) Another way to do this:
        # Automate the task of finding out whether each image (as listed in "pics") exists in the "images" directory. 
        # Use a for loop and if statements to print "cat1.jpg was found!", "cat2.jpg was found!"... etc. 
        # Raise an exception if an image does not exist.

count = 0
for pic in pics:
    if pics == ims_in_dir:
        count = count + 1 
        pic = ims_in_dir
        print ('cat%i.jpg was found!' %count)
    else:
        raise Exception("The image lists do not match up!")

#-create counterbalanced list of all conditions *
catimgs = list(zip(cats, imgs))
print(catimgs)


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
mon = monitors.Monitor('myMonitor', width=35.89, distance=60) 
mon.setSizePix([1440,900])
mon.save()
thisSize = mon.getSizePix() # --> these 3 were for the alternation of stimuli n 4 quadrants
thisWidth = thisSize[0]
thisHeight = thisSize[1]
horizMult = [-1, 1, 1, -1, -1, 1, 1, -1, -1, 1]
vertMult = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1]
CorrectResponse = [True, True, True, True, True, True, True, True, True, True]

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size=(1440,900), color=[0.6, 0.7, 0.8], units = "height", fullscr = True)

#-define experiment start text unsing psychopy functions
start_message = "Welcome to the experiment"
my_textStart = visual.TextStim(win, text=start_message)

#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block"
my_textBlock = visual.TextStim(win, text=block_msg)
end_trial_msg = "End of Trial"
my_textEnd = visual.TextStim(win, text=end_trial_msg)


#-define stimuli using psychopy functions
fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win, units = "pix", size = (400, 400))

#-create response time clock
block_timer = core.Clock()
trial_timer = core.Clock()
# wait_timer = core.Clock()
# clock_wait_timer = core.CountdownTimer()
stimulus_timer = core.Clock()
response_timer = core.Clock()

#-make mouse pointer invisible


#=====================
#START EXPERIMENT
#=====================
#-present start message text
my_textStart.draw()
win.flip()

#-allow participant to begin experiment with button press
my_textBlock.draw()
win.flip()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for thisBlock in range(nBlocks):
    #-present block start message
    print('Welcome to block' + str(thisBlock+1))
    #-randomize order of trials here *
    np.random.shuffle(catimgs)
    #-reset response time clock here
    block_timer.reset()
    block_timer_start = block_timer.getTime()
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for thisTrial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        print('Trial' + str(thisTrial+1))
        #-reset response time clock here
        trial_timer.reset()
        trial_timer_start = trial_timer.getTime()
        #-empty keypresses
        count = -1
        
        
        #=====================
        #START TRIAL
        #=====================   
        stimulus_timer.reset()
        while stimulus_timer.getTime() <= 1: 
        #-draw fixation
            fix_text.draw()
        #-flip window
            win.flip()
        #-wait time (stimulus duration)
            # core.wait(.5)
        
        stimulus_timer.reset()
        response_timer.reset()
        startTime = stimulus_timer.getTime()
        while stimulus_timer.getTime() <= 2:
        #-draw image
            my_image.image = os.path.join(image_dir, pics[thisTrial])
            my_image.pos = (horizMult[thisTrial] * thisWidth/4, vertMult[thisTrial] * thisHeight/4)
            my_image.draw()
            fix_text.draw()
        #-flip window
            win.flip()
        #-collect subject response for that trial
            key = event.waitKeys(maxWait = (response_timer.getTime() <= 2), timeStamped = response_timer)
            if key:
                count=count+1 #count up the number of times a key is pressed
                if count == 0: #if this is the first time a key is pressed
                    print(key)
                    
        #-wait time (stimulus duration)
        endTime = stimulus_timer.getTime()
        
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw stimulus
        #-...
        
        #-collect subject response time for that trial
        print("The test took {} sec." .format(endTime - startTime)) 
        
        #-collect accuracy for that trial
        #if key[0] == 'left':
            #if horizMult[thisTrial] == -1:
                #CorrectResponse[thisTrial] = True
            #else:
                #CorrectResponse[thisTrial] = False
        # if key[0] == 'right':
            #if horizMult[thisTrial] == 1:
                #CorrectResponse[thisTrial] = True
            #else:
                #CorrectResponse[thisTrial] = False
        
        #-draw end trial text
        stimulus_timer.reset()
        while stimulus_timer.getTime() <= 1:
            my_textEnd.draw()
        #-flip window
            win.flip()
        #-wait time (stimulus duration)
            # core.wait(.5)
        
        trial_end_time = trial_timer.getTime()
    
    block_end_time = block_timer.getTime()    
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
win.close()

#-quit experiment
```
This was my output (I also double checked this by pressing the keys multiple times in each trial, but it only recorded the first time I pressed it):
```
###### Running: /Users/kasti/Desktop/PSYCH 403/Assignments/Assignment7.py ######
2022-12-03 15:48:51.156 python[86736:10778855] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignments
/Users/kasti/Desktop/PSYCH 403/Assignments
All variables have been created! Now ready to show the dialog box!
{'subject_nr': 0, 'age': 0, 'handedness': ('right', 'left', 'ambi'), 'gender': (), 'session': 1}
All variables have been created! Now ready to show the dialog box!
15-3-12-2022
['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
cat1.jpg was found!
cat2.jpg was found!
cat3.jpg was found!
cat4.jpg was found!
cat5.jpg was found!
cat6.jpg was found!
cat7.jpg was found!
cat8.jpg was found!
cat9.jpg was found!
cat10.jpg was found!
[('faces', 'im1.png'), ('faces', 'im2.png'), ('faces', 'im3.png'), ('faces', 'im4.png'), ('faces', 'im5.png'), ('faces', 'im6.png'), ('faces', 'im7.png'), ('faces', 'im8.png'), ('faces', 'im9.png'), ('faces', 'im10.png')]
Welcome to block1
Trial1
The test took 2.0425316349137574 sec.
Trial2
[['right', 0.19952150504104793]]
The test took 2.3974182209931314 sec.
Welcome to block2
Trial1
[['left', 0.40868456079624593]]
The test took 2.437658107141033 sec.
Trial2
[['right', 1.1735229259356856]]
The test took 2.191165911965072 sec.
################ Experiment ended with exit code 0 [pid:86736] #################

```
2. Statement placement in your script is very important when collecting responses and refreshing keypresses. What happens if you put event.ClearEvents within the trial loop instead of outside the trial loop? What happens if you unindent the "if keys:" line?

First I put "event.clearEvents()" inside the "for trial" loop in my code I pasted in question #1. The output that I got was the same. 
                
```
#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for thisBlock in range(nBlocks):
    #-present block start message
    print('Welcome to block' + str(thisBlock+1))
    #-randomize order of trials here *
    np.random.shuffle(catimgs)
    #-reset response time clock here
    block_timer.reset()
    block_timer_start = block_timer.getTime()
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    
    for thisTrial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        print('Trial' + str(thisTrial+1))
        #-reset response time clock here
        trial_timer.reset()
        trial_timer_start = trial_timer.getTime()
        #-empty keypresses
        count = -1
        
        
        #=====================
        #START TRIAL
        #=====================   
        stimulus_timer.reset()
        while stimulus_timer.getTime() <= 1: 
        #-draw fixation
            fix_text.draw()
        #-flip window
            win.flip()
        #-wait time (stimulus duration)
            # core.wait(.5)
        
        stimulus_timer.reset()
        response_timer.reset()
        startTime = stimulus_timer.getTime()
        while stimulus_timer.getTime() <= 2:
        #-draw image
            my_image.image = os.path.join(image_dir, pics[thisTrial])
            my_image.pos = (horizMult[thisTrial] * thisWidth/4, vertMult[thisTrial] * thisHeight/4)
            my_image.draw()
            fix_text.draw()
        #-flip window
            win.flip()
        #-collect subject response for that trial
            event.clearEvents()
            key = event.waitKeys(maxWait = (response_timer.getTime() <= 2), timeStamped = response_timer)
            if key:
                count=count+1 #count up the number of times a key is pressed
                if count == 0: #if this is the first time a key is pressed
                    print(key)
                
        #-wait time (stimulus duration)
        endTime = stimulus_timer.getTime()
        
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw stimulus
        #-...
        
        #-collect subject response time for that trial
        print("The test took {} sec." .format(endTime - startTime)) 
        
        #-collect accuracy for that trial
        #if key[0] == 'left':
            #if horizMult[thisTrial] == -1:
                #CorrectResponse[thisTrial] = True
            #else:
                #CorrectResponse[thisTrial] = False
        # if key[0] == 'right':
            #if horizMult[thisTrial] == 1:
                #CorrectResponse[thisTrial] = True
            #else:
                #CorrectResponse[thisTrial] = False
        
        #-draw end trial text
        stimulus_timer.reset()
        while stimulus_timer.getTime() <= 1:
            my_textEnd.draw()
        #-flip window
            win.flip()
        #-wait time (stimulus duration)
            # core.wait(.5)
        
        trial_end_time = trial_timer.getTime()
    
    block_end_time = block_timer.getTime() 

```
Then I put "event.clearEvents()" outside the "for trial" loop in my code I pasted in question #1. The output that I got was, again, the same. 

```
#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for thisBlock in range(nBlocks):
    #-present block start message
    print('Welcome to block' + str(thisBlock+1))
    #-randomize order of trials here *
    np.random.shuffle(catimgs)
    #-reset response time clock here
    block_timer.reset()
    block_timer_start = block_timer.getTime()
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    event.clearEvents()
    for thisTrial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        print('Trial' + str(thisTrial+1))
        #-reset response time clock here
        trial_timer.reset()
        trial_timer_start = trial_timer.getTime()
        #-empty keypresses
        count = -1
        
        
        #=====================
        #START TRIAL
        #=====================   
        stimulus_timer.reset()
        while stimulus_timer.getTime() <= 1: 
        #-draw fixation
            fix_text.draw()
        #-flip window
            win.flip()
        #-wait time (stimulus duration)
            # core.wait(.5)
        
        stimulus_timer.reset()
        response_timer.reset()
        startTime = stimulus_timer.getTime()
        while stimulus_timer.getTime() <= 2:
        #-draw image
            my_image.image = os.path.join(image_dir, pics[thisTrial])
            my_image.pos = (horizMult[thisTrial] * thisWidth/4, vertMult[thisTrial] * thisHeight/4)
            my_image.draw()
            fix_text.draw()
        #-flip window
            win.flip()
        #-collect subject response for that trial
            
            key = event.waitKeys(maxWait = (response_timer.getTime() <= 2), timeStamped = response_timer)
            if key:
                count=count+1 #count up the number of times a key is pressed
                if count == 0: #if this is the first time a key is pressed
                    print(key)
                
        #-wait time (stimulus duration)
        endTime = stimulus_timer.getTime()
        
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw stimulus
        #-...
        
        #-collect subject response time for that trial
        print("The test took {} sec." .format(endTime - startTime)) 
        
        #-collect accuracy for that trial
        #if key[0] == 'left':
            #if horizMult[thisTrial] == -1:
                #CorrectResponse[thisTrial] = True
            #else:
                #CorrectResponse[thisTrial] = False
        # if key[0] == 'right':
            #if horizMult[thisTrial] == 1:
                #CorrectResponse[thisTrial] = True
            #else:
                #CorrectResponse[thisTrial] = False
        
        #-draw end trial text
        stimulus_timer.reset()
        while stimulus_timer.getTime() <= 1:
            my_textEnd.draw()
        #-flip window
            win.flip()
        #-wait time (stimulus duration)
            # core.wait(.5)
        
        trial_end_time = trial_timer.getTime()
    
    block_end_time = block_timer.getTime() 
```
When I unindented the "if keys:" statement, there was no response printed in my output (output is pasted below):
```
###### Running: /Users/kasti/Desktop/PSYCH 403/Assignments/Assignment7.py ######
2022-12-03 16:28:47.473 python[87121:10819101] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignments
/Users/kasti/Desktop/PSYCH 403/Assignments
All variables have been created! Now ready to show the dialog box!
{'subject_nr': 0, 'age': 0, 'handedness': ('right', 'left', 'ambi'), 'gender': (), 'session': 1}
All variables have been created! Now ready to show the dialog box!
16-3-12-2022
['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
cat1.jpg was found!
cat2.jpg was found!
cat3.jpg was found!
cat4.jpg was found!
cat5.jpg was found!
cat6.jpg was found!
cat7.jpg was found!
cat8.jpg was found!
cat9.jpg was found!
cat10.jpg was found!
[('faces', 'im1.png'), ('faces', 'im2.png'), ('faces', 'im3.png'), ('faces', 'im4.png'), ('faces', 'im5.png'), ('faces', 'im6.png'), ('faces', 'im7.png'), ('faces', 'im8.png'), ('faces', 'im9.png'), ('faces', 'im10.png')]
Welcome to block1
Trial1
The test took 2.04748394805938 sec.
Trial2
The test took 2.535051153972745 sec.
Welcome to block2
Trial1
The test took 2.4860871999990195 sec.
Trial2
The test took 2.8507503459695727 sec.
################ Experiment ended with exit code 0 [pid:87121] #################

```

# Recording data exercises

This was my code:
```
from psychopy import core, event, visual, monitors
import numpy as np

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists and dictionary for responses
sub_resp = dict()
sub_acc = dict()
prob = dict()
corr_resp = dict()
resp_time = dict()

my_dict = {'key name':sub_resp, 'subject RT':resp_time, 'subject accuracy':sub_acc, 'correct responses':corr_resp}


#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    sub_resp[block] = [-1]*nTrials
    sub_acc[block] = [-1]*nTrials
    prob[block] = [-1]*nTrials
    corr_resp[block] = [-1]*nTrials
    resp_time[block] = [-1]*nTrials
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial])

print(sub_resp, sub_acc, prob, corr_resp, resp_time)
print(my_dict)
win.close()
```
This was my output:
```
####### Running: /Users/kasti/Desktop/PSYCH 403/Assignments/untitled.py ########
2022-12-03 17:17:49.821 python[87560:10866231] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('4-1=', 3) correct response= 3 subject response= 1 subject accuracy= 2
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('4-1=', 3) correct response= 3 subject response= -1 subject accuracy= 2
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('3-2=', 1) correct response= 1 subject response= 1 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('1+3=', 4) correct response= 4 subject response= 1 subject accuracy= 2
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('3-2=', 1) correct response= 1 subject response= 1 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('4-1=', 3) correct response= 3 subject response= 1 subject accuracy= 2
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('1+3=', 4) correct response= 4 subject response= 1 subject accuracy= 2
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('4-1=', 3) correct response= 3 subject response= 1 subject accuracy= 2
{0: ['1', -1, '1', '1'], 1: ['1', '1', '1', '1']} {0: [2, 2, 1, 2], 1: [1, 2, 2, 2]} {0: [('4-1=', 3), ('4-1=', 3), ('3-2=', 1), ('1+3=', 4)], 1: [('3-2=', 1), ('4-1=', 3), ('1+3=', 4), ('4-1=', 3)]} {0: [3, 3, 1, 4], 1: [1, 3, 4, 3]} {0: [1.2673169139306992, -1, 0.30662115500308573, 1.887225184822455], 1: [1.2509374341461807, 0.36895859404467046, 1.4515610770322382, 0.46928669908083975]}
{'key name': {0: ['1', -1, '1', '1'], 1: ['1', '1', '1', '1']}, 'subject RT': {0: [1.2673169139306992, -1, 0.30662115500308573, 1.887225184822455], 1: [1.2509374341461807, 0.36895859404467046, 1.4515610770322382, 0.46928669908083975]}, 'subject accuracy': {0: [2, 2, 1, 2], 1: [1, 2, 2, 2]}, 'correct responses': {0: [3, 3, 1, 4], 1: [1, 3, 4, 3]}}
################ Experiment ended with exit code 0 [pid:87560] #################
```

# Save csv exercises

1. Using csv.DictWriter (use your favorite search engine to find the help page), save your dictionary (that you created above) as a .csv file.

```
from psychopy import core, event, visual, monitors
import numpy as np
import csv
import os

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

filename = 'subject1session1Nov28.csv'
main_dir = os.getcwd() #define the main directory where experiment info is stored
data_dir = os.path.join(main_dir,'data',filename)
print(data_dir)

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists and dictionary for responses
sub_resp = dict()
sub_acc = dict()
prob = dict()
corr_resp = dict()
resp_time = dict()

my_dict = {'key name':sub_resp, 'subject RT':resp_time, 'subject accuracy':sub_acc, 'correct responses':corr_resp}

data_as_list = [sub_resp, sub_acc, prob, corr_resp, resp_time]

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    sub_resp[block] = [-1]*nTrials
    sub_acc[block] = [-1]*nTrials
    prob[block] = [-1]*nTrials
    corr_resp[block] = [-1]*nTrials
    resp_time[block] = [-1]*nTrials
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial])


with open(data_dir, mode = 'w') as sub_data:
    data_writer = csv.writer(sub_data, delimiter = ',')
    data_writer.writerow(data_as_list)
    
win.close()

```
This was my output:
```
####### Running: /Users/kasti/Desktop/PSYCH 403/Assignments/untitled.py ########
2022-12-03 17:45:35.206 python[87840:10895262] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignments/data/subject1session1Nov28.csv
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('4-1=', 3) correct response= 3 subject response= 1 subject accuracy= 2
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('1+3=', 4) correct response= 4 subject response= 1 subject accuracy= 2
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('1+3=', 4) correct response= 4 subject response= 1 subject accuracy= 2
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('1+1=', 2) correct response= 2 subject response= 1 subject accuracy= 2
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('3-2=', 1) correct response= 1 subject response= 1 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('3-2=', 1) correct response= 1 subject response= 1 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('4-1=', 3) correct response= 3 subject response= 1 subject accuracy= 2
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('4-1=', 3) correct response= 3 subject response= 1 subject accuracy= 2
################ Experiment ended with exit code 0 [pid:87840] #################
```
This was the excel sheet output:
{0: ['1', '1', '1', '1'], 1: ['1', '1', '1', '1']}	{0: [2, 2, 2, 2], 1: [1, 1, 2, 2]}	{0: [('4-1=', 3), ('1+3=', 4), ('1+3=', 4), ('1+1=', 2)], 1: [('3-2=', 1), ('3-2=', 1), ('4-1=', 3), ('4-1=', 3)]}	{0: [3, 4, 4, 2], 1: [1, 1, 3, 3]}	{0: [0.9540578620508313, 2.3404440919402987, 0.6197542028967291, 0.34875560319051147], 1: [0.3011722059454769, 0.21794727491214871, 0.6682008188217878, 0.6836525141261518]}

# Save JSON exercises

1. Add JSON filesaving to your experiment script.
```
from psychopy import core, event, visual, monitors
import numpy as np
import csv
import os
import json as json

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

filename = 'subject1session1Nov28.csv'
main_dir = os.getcwd() #define the main directory where experiment info is stored
data_dir = os.path.join(main_dir,'data',filename)
print(data_dir)

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists and dictionary for responses
sub_resp = dict()
sub_acc = dict()
prob = dict()
corr_resp = dict()
resp_time = dict()

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    sub_resp[block] = [-1]*nTrials
    sub_acc[block] = [-1]*nTrials
    prob[block] = [-1]*nTrials
    corr_resp[block] = [-1]*nTrials
    resp_time[block] = [-1]*nTrials
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial])

for block in range(nBlocks):
    data_as_dict = []
    for a,b,c,d,e in zip(prob[block], corr_resp[block], sub_resp[block], sub_acc[block], resp_time[block]):
        #the names listed here do not need to be the same as the variable names
        data_as_dict.append({'problem':a,'corr_resp':b,'sub_resp':c,'sub_acc':d, 'resp_time':e})
    print(data_as_dict)     
    
    with open(filename + '_block%i.txt'%block, 'w') as outfile:
        json.dump(data_as_dict, outfile)
win.close()

```
This was my ouput: 
```
####### Running: /Users/kasti/Desktop/PSYCH 403/Assignments/untitled.py ########
2022-12-03 17:53:50.711 python[87932:10905077] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignments/data/subject1session1Nov28.csv
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('1+3=', 4) correct response= 4 subject response= 4 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('1+1=', 2) correct response= 2 subject response= 2 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('1+1=', 2) correct response= 2 subject response= 2 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('4-1=', 3) correct response= 3 subject response= 3 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('1+3=', 4) correct response= 4 subject response= 4 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('4-1=', 3) correct response= 3 subject response= 3 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('4-1=', 3) correct response= 3 subject response= -1 subject accuracy= 2
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('3-2=', 1) correct response= 1 subject response= 1 subject accuracy= 1
[{'problem': ('1+3=', 4), 'corr_resp': 4, 'sub_resp': '4', 'sub_acc': 1, 'resp_time': 1.4276396499481052}, {'problem': ('1+1=', 2), 'corr_resp': 2, 'sub_resp': '2', 'sub_acc': 1, 'resp_time': 0.9839523020200431}, {'problem': ('1+1=', 2), 'corr_resp': 2, 'sub_resp': '2', 'sub_acc': 1, 'resp_time': 0.5886133469175547}, {'problem': ('4-1=', 3), 'corr_resp': 3, 'sub_resp': '3', 'sub_acc': 1, 'resp_time': 1.2506037901621312}]
[{'problem': ('1+3=', 4), 'corr_resp': 4, 'sub_resp': '4', 'sub_acc': 1, 'resp_time': 1.0338230631314218}, {'problem': ('4-1=', 3), 'corr_resp': 3, 'sub_resp': '3', 'sub_acc': 1, 'resp_time': 1.0505026141181588}, {'problem': ('4-1=', 3), 'corr_resp': 3, 'sub_resp': -1, 'sub_acc': 2, 'resp_time': -1}, {'problem': ('3-2=', 1), 'corr_resp': 1, 'sub_resp': '1', 'sub_acc': 1, 'resp_time': 1.0503099078778177}]
################ Experiment ended with exit code 0 [pid:87932] #################
```
# Read JSON exercises

1 and 2.
```
from psychopy import core, event, visual, monitors
import numpy as np
import csv
import os
import json as json
import pandas as pd

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

filename = 'subject1session1Nov28.csv'
main_dir = os.getcwd() #define the main directory where experiment info is stored
data_dir = os.path.join(main_dir,'data',filename)
print(data_dir)


#blocks, trials, stims, and clocks
nBlocks=1
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists and dictionary for responses
sub_resp = dict()
sub_acc = dict()
prob = dict()
corr_resp = dict()
resp_time = dict()

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    sub_resp[block] = [-1]*nTrials
    sub_acc[block] = [-1]*nTrials
    prob[block] = [-1]*nTrials
    corr_resp[block] = [-1]*nTrials
    resp_time[block] = [-1]*nTrials
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial])

for block in range(nBlocks):
    data_as_dict = []
    for a,b,c,d,e in zip(prob[block], corr_resp[block], sub_resp[block], sub_acc[block], resp_time[block]):
        #the names listed here do not need to be the same as the variable names
        data_as_dict.append({'problem':a,'corr_resp':b,'sub_resp':c,'sub_acc':d, 'resp_time':e})
    print(data_as_dict)     
    
    with open(filename + '_block%i.txt'%block, 'w') as outfile:
        json.dump(data_as_dict, outfile)

print("This is the saved JSON file as a formatted table")
df = pd.read_json(filename+'_block1.txt')
print(df)

print("This is the rudimentary analyses on the data")
print("Pearson r:")
print(pd.DataFrame.corr(df,method='pearson'))
print("Spearman rho:")
print(pd.DataFrame.corr(df,method='spearman'))

print("These are the trials with correct responses")
acc_trials = df.loc[df['sub_acc'] == 1]
print(acc_trials)

print("These are the means")

print("Average Response Time for all responses")
print(sum(df['resp_time'])/len(df['resp_time']))

print("Average Subject accuracy for all responses")
print(sum(df['sub_acc'])/len(df['sub_acc']))

win.close()
```

Output:
```
####### Running: /Users/kasti/Desktop/PSYCH 403/Assignments/untitled.py ########
2022-12-03 18:36:51.571 python[88309:10948564] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignments/data/subject1session1Nov28.csv
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('3-2=', 1) correct response= 1 subject response= 1 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('3-2=', 1) correct response= 1 subject response= 1 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('4-1=', 3) correct response= 3 subject response= 3 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('3-2=', 1) correct response= 1 subject response= 1 subject accuracy= 1
[{'problem': ('3-2=', 1), 'corr_resp': 1, 'sub_resp': '1', 'sub_acc': 1, 'resp_time': 0.9845419470220804}, {'problem': ('3-2=', 1), 'corr_resp': 1, 'sub_resp': '1', 'sub_acc': 1, 'resp_time': 0.5044161221012473}, {'problem': ('4-1=', 3), 'corr_resp': 3, 'sub_resp': '3', 'sub_acc': 1, 'resp_time': 1.0668617861811072}, {'problem': ('3-2=', 1), 'corr_resp': 1, 'sub_resp': '1', 'sub_acc': 1, 'resp_time': 1.2678321588318795}]
This is the saved JSON file as a formatted table
     problem  corr_resp  sub_resp  sub_acc  resp_time
0  [1+1=, 2]          2         2        1   1.083051
1  [4-1=, 3]          3         3        1   0.969050
2  [1+1=, 2]          2         2        1   0.851534
3  [1+3=, 4]          4         4        1   0.935708
This is the rudimentary analyses on the data
Pearson r:
           corr_resp  sub_resp  sub_acc  resp_time
corr_resp   1.000000  1.000000      NaN  -0.141766
sub_resp    1.000000  1.000000      NaN  -0.141766
sub_acc          NaN       NaN      NaN        NaN
resp_time  -0.141766 -0.141766      NaN   1.000000
Spearman rho:
           corr_resp  sub_resp  sub_acc  resp_time
corr_resp   1.000000  1.000000      NaN  -0.105409
sub_resp    1.000000  1.000000      NaN  -0.105409
sub_acc          NaN       NaN      NaN        NaN
resp_time  -0.105409 -0.105409      NaN   1.000000
These are the trials with correct responses
     problem  corr_resp  sub_resp  sub_acc  resp_time
0  [1+1=, 2]          2         2        1   1.083051
1  [4-1=, 3]          3         3        1   0.969050
2  [1+1=, 2]          2         2        1   0.851534
3  [1+3=, 4]          4         4        1   0.935708
These are the means
Average Response Time for all responses
0.9598357893992213
Average Subject accuracy for all responses
1.0
################ Experiment ended with exit code 0 [pid:88309] #################
```

```
from psychopy import core, event, visual, monitors
import numpy as np
import csv
import os
import json as json
import pandas as pd

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

filename = 'subject1session1Nov28.csv'
main_dir = os.getcwd() #define the main directory where experiment info is stored
data_dir = os.path.join(main_dir,'data',filename)
print(data_dir)


#blocks, trials, stims, and clocks
nBlocks=1
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists and dictionary for responses
sub_resp = dict()
sub_acc = dict()
prob = dict()
corr_resp = dict()
resp_time = dict()

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    sub_resp[block] = [-1]*nTrials
    sub_acc[block] = [-1]*nTrials
    prob[block] = [-1]*nTrials
    corr_resp[block] = [-1]*nTrials
    resp_time[block] = [-1]*nTrials
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial])

for block in range(nBlocks):
    data_as_dict = []
    for a,b,c,d,e in zip(prob[block], corr_resp[block], sub_resp[block], sub_acc[block], resp_time[block]):
        #the names listed here do not need to be the same as the variable names
        data_as_dict.append({'problem':a,'corr_resp':b,'sub_resp':c,'sub_acc':d, 'resp_time':e})
    print(data_as_dict)     
    
    with open(filename + '_block%i.txt'%block, 'w') as outfile:
        json.dump(data_as_dict, outfile)

print("This is the saved JSON file as a formatted table")
df = pd.read_json(filename+'_block1.txt')
print(df)

print("This is the rudimentary analyses on the data")
print("Pearson r:")
print(pd.DataFrame.corr(df,method='pearson'))
print("Spearman rho:")
print(pd.DataFrame.corr(df,method='spearman'))

print("These are the trials with correct responses")
acc_trials = df.loc[df['sub_acc'] != 0]
print(acc_trials)

print("These are the means")

print("Average Response Time for all responses")
print(sum(df['resp_time'])/len(df['resp_time']))

print("Average Subject accuracy for all responses")
print(sum(df['sub_acc'])/len(df['sub_acc']))

win.close()
```
3. 

```
from psychopy import core, event, visual, monitors
import numpy as np
import csv
import os
import json as json
import pandas as pd

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

filename = 'subject1session1Nov28.csv'
main_dir = os.getcwd() #define the main directory where experiment info is stored
data_dir = os.path.join(main_dir,'data',filename)
print(data_dir)


#blocks, trials, stims, and clocks
nBlocks=1
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists and dictionary for responses
sub_resp = dict()
sub_acc = dict()
prob = dict()
corr_resp = dict()
resp_time = dict()

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    sub_resp[block] = [-1]*nTrials
    sub_acc[block] = [-1]*nTrials
    prob[block] = [-1]*nTrials
    corr_resp[block] = [-1]*nTrials
    resp_time[block] = [-1]*nTrials
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial])

for block in range(nBlocks):
    data_as_dict = []
    for a,b,c,d,e in zip(prob[block], corr_resp[block], sub_resp[block], sub_acc[block], resp_time[block]):
        #the names listed here do not need to be the same as the variable names
        data_as_dict.append({'problem':a,'corr_resp':b,'sub_resp':c,'sub_acc':d, 'resp_time':e})
    print(data_as_dict)     
    
    with open(filename + '_block%i.txt'%block, 'w') as outfile:
        json.dump(data_as_dict, outfile)

print("This is the saved JSON file as a formatted table")
df = pd.read_json(filename+'_block1.txt')
print(df)

print("This is the rudimentary analyses on the data")
print("Pearson r:")
print(pd.DataFrame.corr(df,method='pearson'))
print("Spearman rho:")
print(pd.DataFrame.corr(df,method='spearman'))

print("These are the trials with correct responses")
acc_trials = df.loc[df['sub_acc'] != 1]
print(acc_trials)

print("These are the means")

print("Average Response Time for all responses")
print(sum(df['resp_time'])/len(df['resp_time']))

print("Average Subject accuracy for all responses")
print(sum(df['sub_acc'])/len(df['sub_acc']))

print("Average Response Time for correct responses")
print(len(acc_trials)/len(df['sub_resp']))

print("Average Subject accuracy for correct responses")
print(len(acc_trials)/len(df['sub_acc']))


win.close()

```
Output:
```
####### Running: /Users/kasti/Desktop/PSYCH 403/Assignments/untitled.py ########
2022-12-03 18:47:59.329 python[88414:10957420] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignments/data/subject1session1Nov28.csv
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('1+1=', 2) correct response= 2 subject response= 2 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('1+3=', 4) correct response= 4 subject response= -1 subject accuracy= 2
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('1+1=', 2) correct response= 2 subject response= 2 subject accuracy= 1
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
problem= ('1+1=', 2) correct response= 2 subject response= 2 subject accuracy= 1
[{'problem': ('1+1=', 2), 'corr_resp': 2, 'sub_resp': '2', 'sub_acc': 1, 'resp_time': 1.0461644518654794}, {'problem': ('1+3=', 4), 'corr_resp': 4, 'sub_resp': -1, 'sub_acc': 2, 'resp_time': -1}, {'problem': ('1+1=', 2), 'corr_resp': 2, 'sub_resp': '2', 'sub_acc': 1, 'resp_time': 0.9375864830799401}, {'problem': ('1+1=', 2), 'corr_resp': 2, 'sub_resp': '2', 'sub_acc': 1, 'resp_time': 1.0003600700292736}]
This is the saved JSON file as a formatted table
     problem  corr_resp  sub_resp  sub_acc  resp_time
0  [1+1=, 2]          2         2        1   1.083051
1  [4-1=, 3]          3         3        1   0.969050
2  [1+1=, 2]          2         2        1   0.851534
3  [1+3=, 4]          4         4        1   0.935708
This is the rudimentary analyses on the data
Pearson r:
           corr_resp  sub_resp  sub_acc  resp_time
corr_resp   1.000000  1.000000      NaN  -0.141766
sub_resp    1.000000  1.000000      NaN  -0.141766
sub_acc          NaN       NaN      NaN        NaN
resp_time  -0.141766 -0.141766      NaN   1.000000
Spearman rho:
           corr_resp  sub_resp  sub_acc  resp_time
corr_resp   1.000000  1.000000      NaN  -0.105409
sub_resp    1.000000  1.000000      NaN  -0.105409
sub_acc          NaN       NaN      NaN        NaN
resp_time  -0.105409 -0.105409      NaN   1.000000
These are the trials with correct responses
Empty DataFrame
Columns: [problem, corr_resp, sub_resp, sub_acc, resp_time]
Index: []
These are the means
Average Response Time for all responses
0.9598357893992213
Average Subject accuracy for all responses
1.0
Average Response Time for correct responses
0.0
Average Subject accuracy for correct responses
0.0
################ Experiment ended with exit code 0 [pid:88414] #################

```
