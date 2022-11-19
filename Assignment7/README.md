# Wait Exercises

1. Fill in the following pseudocode with the real code you have learned so far using "core.wait" (and run it to make sure it works):
```
        #=====================
        #START TRIAL
        #===================== 
        #-draw fixation
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw image
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw end trial text
        #-flip window
        #-wait time (stimulus duration)
```
This was my code
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
nTrials = 10
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
    
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for thisTrial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        print('Trial' + str(thisTrial+1))
        
        #-empty keypresses
        
        
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5)
        
        #-draw image
        my_image.image = os.path.join(image_dir, pics[thisTrial])
        my_image.pos = (horizMult[thisTrial] * thisWidth/4, vertMult[thisTrial] * thisHeight/4)
        my_image.draw()
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5)
    
        #-draw end trial text
        my_textEnd.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5)
        
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
win.close()

#-quit experiment
```


# Clock exercises

1. Create a "wait_timer" to find out exactly how long core.wait(2) presents each image. Make sure this is not counting the time of the whole trial, but only the duration of each image. How precise is core.wait?

Answer: I noticed that in my output, the accuracy was pretty good, give or take 1 msec. 
 
This was my code for this question:

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
nTrials = 10
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
    
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for thisTrial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        print('Trial' + str(thisTrial+1))
        #-empty keypresses
        
        
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5)
        
        #-draw image
        my_image.image = os.path.join(image_dir, pics[thisTrial])
        my_image.pos = (horizMult[thisTrial] * thisWidth/4, vertMult[thisTrial] * thisHeight/4)
        my_image.draw()
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        wait_timer = core.Clock()
        startTime = wait_timer.getTime()
        core.wait(.5) 
        endTime = wait_timer.getTime()
        print("The test took {} msec." .format(1000*endTime)) 
        
    
        #-draw end trial text
        my_textEnd.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(.5)
        
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
win.close()

#-quit experiment
```
And this was my output for the code above
```
###### Running: /Users/kasti/Desktop/PSYCH 403/Assignments/Assignment7.py ######
2022-11-19 15:27:29.436 python[76914:4768366] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignments
/Users/kasti/Desktop/PSYCH 403/Assignments
All variables have been created! Now ready to show the dialog box!
{'subject_nr': 0, 'age': 0, 'handedness': ('right', 'left', 'ambi'), 'gender': (), 'session': 1}
All variables have been created! Now ready to show the dialog box!
15-19-11-2022
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
The test took 501.2665300164372 msec.
Trial2
The test took 501.2718699872494 msec.
Trial3
The test took 501.24672695528716 msec.
Trial4
The test took 501.2772139161825 msec.
Trial5
The test took 501.30426802206784 msec.
Trial6
The test took 501.23936496675014 msec.
Trial7
The test took 501.22737302444875 msec.
Trial8
The test took 501.2980420142412 msec.
Trial9
The test took 501.2504319893196 msec.
Trial10
The test took 501.20553793385625 msec.
Welcome to block2
Trial1
The test took 501.19034794624895 msec.
Trial2
The test took 500.5417199572548 msec.
Trial3
The test took 501.13850401248783 msec.
Trial4
The test took 501.2458099517971 msec.
Trial5
The test took 501.1850739829242 msec.
Trial6
The test took 501.2184929801151 msec.
Trial7
The test took 501.00424501579255 msec.
Trial8
The test took 501.1973229702562 msec.
Trial9
The test took 501.23841408640146 msec.
Trial10
The test took 501.27805990632623 msec.
################ Experiment ended with exit code 0 [pid:76914] #################
```


2. Create a "clock_wait_timer" to find out exactly how long each image is presented when you use a clock + while loops. How precise is this?

3. Create a "countdown_timer" to find out exactly how long each image is presented when you use a CountdownTimer + while loops. How precise is this?

4. Edit your main experiment script so that the trials loop according to a clock timer. Also create and implement a block_timer and a trial_timer.



# Frame-based timing exercises
1. Adjust your experiment so that it follows frame-based timing rather than clock timing (comment out the clock-based timing code in case you want to use it again) using for loops and if statements.

2. Add a "dropped frame" detector to your script to find out whether your experiment is dropping frames. How many total frames are dropped in the experiment? If 20 or fewer frames are dropped in the whole experiment (1 frame per trial), keep frame-based timing in your experiment. Otherwise, switch back to the CountdownTimer.

