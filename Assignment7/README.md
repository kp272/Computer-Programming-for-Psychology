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
block_timer = core.Clock()
trial_timer = core.Clock()
wait_timer = core.Clock()

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
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for thisTrial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        print('Trial' + str(thisTrial+1))
        #-reset response time clock here
        trial_timer.reset()
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
        startTime = wait_timer.getTime()
        core.wait(2)
        endTime = wait_timer.getTime()
        
        
    
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
        print("The test took {} sec." .format(endTime - startTime)) 
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
2022-11-19 16:26:45.799 python[77415:4801453] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignments
/Users/kasti/Desktop/PSYCH 403/Assignments
All variables have been created! Now ready to show the dialog box!
{'subject_nr': 0, 'age': 0, 'handedness': ('right', 'left', 'ambi'), 'gender': (), 'session': 1}
All variables have been created! Now ready to show the dialog box!
16-19-11-2022
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
The test took 2.001297533046454 sec.
Trial2
The test took 2.001228114007972 sec.
Trial3
The test took 2.001265081926249 sec.
Trial4
The test took 2.0011874650372192 sec.
Trial5
The test took 2.0013348089996725 sec.
Trial6
The test took 2.0012795900693163 sec.
Trial7
The test took 2.0012838259572163 sec.
Trial8
The test took 2.00129908695817 sec.
Trial9
The test took 2.00109037803486 sec.
Trial10
The test took 2.0012204290833324 sec.
Welcome to block2
Trial1
The test took 2.001186672016047 sec.
Trial2
The test took 2.0012548299273476 sec.
Trial3
The test took 2.001210083020851 sec.
Trial4
The test took 2.0012573190033436 sec.
Trial5
The test took 2.000544944079593 sec.
Trial6
The test took 2.0012525129131973 sec.
Trial7
The test took 2.0012748390436172 sec.
Trial8
The test took 2.0012807300081477 sec.
Trial9
The test took 2.00127617304679 sec.
Trial10
The test took 2.0012127809459344 msec.
################ Experiment ended with exit code 0 [pid:77415] #################

```


2. Create a "clock_wait_timer" to find out exactly how long each image is presented when you use a clock + while loops. How precise is this?

This method took longer than the first one, because the difference was of now about 1 - 30 msec.

This was my code:
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
block_timer = core.Clock()
trial_timer = core.Clock()
wait_timer = core.Clock()
clock_wait_timer = core.Clock()

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
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for thisTrial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        print('Trial' + str(thisTrial+1))
        #-reset response time clock here
        trial_timer.reset()
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
        
        clock_wait_timer.reset()
        startTime = wait_timer.getTime()
        while clock_wait_timer.getTime() <=2:
        #-draw image
            my_image.image = os.path.join(image_dir, pics[thisTrial])
            my_image.pos = (horizMult[thisTrial] * thisWidth/4, vertMult[thisTrial] * thisHeight/4)
            my_image.draw()
            fix_text.draw()
        #-flip window
            win.flip()
        #-wait time (stimulus duration)
        endTime = wait_timer.getTime()
        
        
    
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
        print("The test took {} sec." .format(endTime - startTime)) 
        #-collect accuracy for that trial
        
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
win.close()

#-quit experiment
```
This was my output:
```
###### Running: /Users/kasti/Desktop/PSYCH 403/Assignments/Assignment7.py ######
2022-11-19 16:44:41.210 python[77572:4811848] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignments
/Users/kasti/Desktop/PSYCH 403/Assignments
All variables have been created! Now ready to show the dialog box!
{'subject_nr': 0, 'age': 0, 'handedness': ('right', 'left', 'ambi'), 'gender': (), 'session': 1}
All variables have been created! Now ready to show the dialog box!
16-19-11-2022
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
The test took 2.00092310202308 sec.
Trial2
The test took 2.027687667054124 sec.
Trial3
The test took 2.009592536953278 sec.
Trial4
The test took 2.011553360032849 sec.
Trial5
The test took 2.0066935929935426 sec.
Trial6
The test took 2.0065280199050903 sec.
Trial7
The test took 2.0080410899827257 sec.
Trial8
The test took 2.007913374924101 sec.
Trial9
The test took 2.007684299023822 sec.
Trial10
The test took 2.0064346570288762 sec.
Welcome to block2
Trial1
The test took 2.006043661967851 sec.
Trial2
The test took 2.0234206850873306 sec.
Trial3
The test took 2.005862803896889 sec.
Trial4
The test took 2.012936130980961 sec.
Trial5
The test took 2.0089825419709086 sec.
Trial6
The test took 2.0057032839395106 sec.
Trial7
The test took 2.001950348028913 sec.
Trial8
The test took 2.00707767799031 sec.
Trial9
The test took 2.008607789990492 sec.
Trial10
The test took 2.00418703595642 sec.
################ Experiment ended with exit code 0 [pid:77572] #################

```


3. Create a "countdown_timer" to find out exactly how long each image is presented when you use a CountdownTimer + while loops. How precise is this?

This was my code:
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
block_timer = core.Clock()
trial_timer = core.Clock()
wait_timer = core.Clock()
clock_wait_timer = core.CountdownTimer()

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
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for thisTrial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        print('Trial' + str(thisTrial+1))
        #-reset response time clock here
        trial_timer.reset()
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
        
        clock_wait_timer.reset()
        clock_wait_timer.add(2)
        startTime = wait_timer.getTime()
        while clock_wait_timer.getTime() >= 0:
        #-draw image
            my_image.image = os.path.join(image_dir, pics[thisTrial])
            my_image.pos = (horizMult[thisTrial] * thisWidth/4, vertMult[thisTrial] * thisHeight/4)
            my_image.draw()
            fix_text.draw()
        #-flip window
            win.flip()
        #-wait time (stimulus duration)
        endTime = wait_timer.getTime()
        
        
    
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
        print("The test took {} sec." .format(endTime - startTime)) 
        #-collect accuracy for that trial
        
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
win.close()

#-quit experiment
```
This was my output:
```
###### Running: /Users/kasti/Desktop/PSYCH 403/Assignments/Assignment7.py ######
2022-11-27 10:59:15.405 python[39467:8104203] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to /var/folders/f5/p7ypm_qj1tz18rjd6bfnzrwr0000gn/T/org.opensciencetools.psychopy.savedState
/Users/kasti/Desktop/PSYCH 403/Assignments
/Users/kasti/Desktop/PSYCH 403/Assignments
All variables have been created! Now ready to show the dialog box!
{'subject_nr': 0, 'age': 0, 'handedness': ('right', 'left', 'ambi'), 'gender': (), 'session': 1}
All variables have been created! Now ready to show the dialog box!
10-27-11-2022
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
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial1
The test took 2.0129963560029864 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial2
The test took 2.0001714769750834 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial3
The test took 2.0068263489520177 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial4
The test took 2.0083453690167516 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial5
The test took 2.0101114420685917 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial6
The test took 2.005087784025818 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial7
The test took 2.0065269909100607 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial8
The test took 2.0052711779717356 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial9
The test took 2.008043518057093 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial10
The test took 2.015481580980122 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Welcome to block2
Trial1
The test took 2.0063811379950494 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial2
The test took 2.0156946869101375 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial3
The test took 2.0082444800063968 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial4
The test took 2.015683387988247 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial5
The test took 2.0097469120519236 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial6
The test took 2.0105416759615764 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial7
The test took 2.00475693307817 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial8
The test took 2.006855277926661 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial9
The test took 2.006915500969626 sec.
WARNING:root:DEPRECATED: Clock.add() is deprecated in favor of .addTime() due to the counterintuitive design (it added time to the baseline, which reduced the values returned from getTime()
Trial10
The test took 2.010142182931304 sec.
################ Experiment ended with exit code 0 [pid:39467] #################

```

4. Edit your main experiment script so that the trials loop according to a clock timer. Also create and implement a block_timer and a trial_timer.

This was my code:
```

```
This was my output:
```

```

# Frame-based timing exercises
1. Adjust your experiment so that it follows frame-based timing rather than clock timing (comment out the clock-based timing code in case you want to use it again) using for loops and if statements.

2. Add a "dropped frame" detector to your script to find out whether your experiment is dropping frames. How many total frames are dropped in the experiment? If 20 or fewer frames are dropped in the whole experiment (1 frame per trial), keep frame-based timing in your experiment. Otherwise, switch back to the CountdownTimer.

